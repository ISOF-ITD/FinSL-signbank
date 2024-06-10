# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q, Prefetch
from django.db.models.functions import Substr, Upper
from django.templatetags.static import static
from django.utils.translation import ugettext as _
import platform

from signbank.dictionary.forms import GlossPublicSearchForm
#from django.contrib.staticfiles.templatetags.staticfiles import static
#from django.utils.translation import ugettext as _
#from django.views.decorators.cache import cache_page
#from django.shortcuts import get_object_or_404

#from signbank.settings.configuration import Configuration

#from .models import Gloss, Translation, GlossTranslations, SignLanguage, Dataset, GlossRelation, Keyword
from signbank.dictionary.models import Gloss, Dataset, SignLanguage, GlossRelation, Translation, GlossTranslations, Keyword
#from .models import Gloss, Dataset, SignLanguage, GlossRelation, Translation, GlossTranslations, Keyword
#from ..video.models import GlossVideo
from signbank.video.models import GlossVideo
#from .adminviews import serialize_glosses

# ISOF Per
from tagging.models import Tag, TaggedItem

# autocomplete
# from dal import autocomplete
from django.views.generic.edit import FormView
import json
from django.http import HttpResponse

import re

class TranslationServiceView(FormView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        term = data.get("term")
        #Remove not litterals as extra percausion
        name = re.sub(u'[^\wåäö]', "", term)
        # name2 = re.sub(r"[^a-zA-Zå-öÄ-Ö]+", "", term)
        if name:
            # Return keywords
            # glosses = Gloss.objects.filter(idgloss__istartswith = name)
            # translations = Keyword.objects.filter(text__istartswith = name)

            # Return ONLY keywords with published glosses
            sqlselect = '''SELECT dk.id as id, dk.text as text, dg.idgloss, vg.videofile, dg.notes FROM teckensprak.dictionary_keyword dk'''
            sqljoin = ''' JOIN teckensprak.dictionary_translation dt ON dk.id = dt.keyword_id JOIN teckensprak.dictionary_gloss dg ON dg.id = dt.gloss_id JOIN teckensprak.video_glossvideo vg ON dg.id = vg.gloss_id '''

            # https: // groups.google.com / forum /  # !topic/django-users/bma8Qk2T-V4
            sqlfilter2 = " WHERE dg.published = TRUE and vg.is_public = TRUE AND text like %s"
            user_input = "%s%%" % name

            # funkar:
            sql = sqlselect + sqljoin + sqlfilter2

            # Return ONLY keywords with published glosses using objects.raw (no need for extra sql-view or model class)
            translations = Keyword.objects.raw(sql, [user_input])
            # translations = Keyword.objects.raw(sql)
        # else:
            # translations = Keyword.objects.all()
        results = []
        for translation in translations:
            all_json = {}
            all_json['id'] = translation.id
            all_json['question'] = translation.text
            all_json['videofile'] = translation.videofile
            all_json['answer'] = translation.notes
            results.append(all_json)
        data = json.dumps(results)
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)


# *code in view which returns json data *
class TranslationAutoCompleteView(FormView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        term = data.get("term")
        tag = None
        if data.get("tag"):
            tag = data.get("tag")
        #Remove not litterals as extra percausion
        name = re.sub(u'[^\wåäö]', "", term)
        # name2 = re.sub(r"[^a-zA-Zå-öÄ-Ö]+", "", term)
        if name:
            # Return keywords
            # glosses = Gloss.objects.filter(idgloss__istartswith = name)
            # translations = Keyword.objects.filter(text__istartswith = name)

            # Return ONLY keywords with published glosses
            sqlselect = '''SELECT dk.id as id, dk.text as text FROM teckensprak.dictionary_keyword dk'''
            sqljoin = ''' JOIN teckensprak.dictionary_translation dt ON dk.id = dt.keyword_id JOIN teckensprak.dictionary_gloss dg ON dg.id = dt.gloss_id'''
            # sqljoin = ''' JOIN teckensprak.dictionary_translation dt ON dk.id = dt.keyword_id
                                                    # JOIN teckensprak.dictionary_gloss dg ON dg.id = dt.gloss_id'''
                                                    # WHERE dg.published = 1
                                                    # AND upper(dk.text) like upper(%s)'''
            # sqlfilter2 = ''' WHERE dg.published = 1 AND upper(dk.text) like upper(%s)'''
            # sqlfilter2like = " WHERE dg.published = 1 AND text like '" + name + "%';"
            sqlfilter2 = " WHERE dg.published = 1 AND text REGEXP '^" + name + "';"
            # sqlfilter1 = " WHERE text REGEXP '^" + name + "';"
            # sqlfilterparamlike = ''' WHERE dg.published = 1 AND upper(dk.text) like upper(%s)'''
            # sqlfilterparam = " WHERE dg.published = 1 AND text REGEXP '^" + name + "';"
            # sqlfilterparam = " WHERE dg.published = 1 AND text REGEXP '^%s';"

            # https: // groups.google.com / forum /  # !topic/django-users/bma8Qk2T-V4
            sqlfilter2 = " WHERE dg.published = 1 AND text like %s"
            user_input1 = "%s%%" % name
            user_input = [user_input1]

            sqljointag = ""
            sqlfiltertag = ""
            if tag:
                sqljointag = ''' JOIN teckensprak.tagging_taggeditem tt ON tt.object_id = dt.gloss_id JOIN teckensprak.tagging_tag t ON tt.tag_id = t.id'''
                sqlfiltertag = '''  AND t.id = %s '''
                user_input2 = "%s%%" % tag
                user_input = [user_input1, user_input2]

            # funkar:
            # sql = sqlselect + sqljoin + sqlfilter2
            sql = sqlselect + sqljoin + sqljointag + sqlfilter2 + sqlfiltertag
            # sql = sqlselect + sqlfilter1

            # funkar inte:
            # sql = sqlselect + sqljoin + sqlfilter2like
            # sql = sqlselect + sqljoin + sqlfilterparam

            # sql1 = 'SELECT dk.id as id, dk.text as text FROM teckensprak.dictionary_keyword dk WHERE upper(dk.text) like upper(''' + name + '%'')'
            # sql1 = 'SELECT dk.id as id, dk.text as text FROM teckensprak.dictionary_keyword dk WHERE upper(dk.text) like upper("fö%")'
            # sql1 = "SELECT dk.id as id, dk.text as text FROM teckensprak.dictionary_keyword dk WHERE upper(dk.text) like upper("fö%") WHERE text REGEXP '^före';"

            # sql1 = "SELECT dk.id as id, dk.text as text FROM teckensprak.dictionary_keyword dk WHERE text REGEXP '^%s';"
            # sql1 = 'SELECT dk.id as id, dk.text as text FROM teckensprak.dictionary_keyword dk WHERE text REGEXP "^%s";'
            # funkar inte:
            # sql1 = "SELECT dk.id as id, dk.text as text FROM teckensprak.dictionary_keyword dk WHERE dk.text like 'fö%'"
            # Unable to get repr for < class 'django.db.models.query.RawQuerySet' > 'SELECT dk.id as id, dk.text as text FROM teckensprak.dictionary_keyword dk WHERE dk.text like \\'fö%\\''
            # sql1 = 'SELECT dk.id as id, dk.text as text FROM teckensprak.dictionary_keyword dk WHERE dk.text like "fö%"'
            # funkar:
            # sql1 = "SELECT dk.id as id, dk.text as text FROM teckensprak.dictionary_keyword dk WHERE text REGEXP '^" + name + "';"
            # sql1 = 'SELECT dk.id as id, dk.text as text FROM teckensprak.dictionary_keyword dk WHERE text = "förening"'
            # sql1 = 'SELECT dk.id as id, dk.text as text FROM teckensprak.dictionary_keyword dk'

            # Return ONLY keywords with published glosses using objects.raw (no need for extra sql-view or model class)
            translations = Keyword.objects.raw(sql, user_input)
            # translations = Keyword.objects.raw(sql)
        # else:
            # translations = Keyword.objects.all()
        results = []
        for translation in translations:
            all_json = {}
            all_json['id'] = translation.id
            all_json['label'] = translation.text
            all_json['value'] = translation.text
            results.append(all_json)
        data = json.dumps(results)
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)


class TranslationListPublicView(ListView):
    model = Gloss
    # template_name = 'dictionary/public_gloss_list.html'
    template_name = 'dictionary/public_translation_list_v1.html'
    # template_name = 'translation/public_translation_list.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TranslationListPublicView, self).get_context_data(**kwargs)
        #context["searchform"] = None
        # host_name = self.request.get_host()
        # context['computer'] = Configuration.computer
        #context['host_name'] = host_name
        computer_name = platform.node()
        computer = 'utveckling'
        # Server has uu.se in name
        if 'uu.se' in computer_name:
            computer = 'server'
        context['computer'] = computer
        context["searchform"] = GlossPublicSearchForm(self.request.GET)
        context["signlanguages"] = SignLanguage.objects.filter(dataset__is_public=True).distinct()
        context["signlanguage_count"] = context["signlanguages"].count()
        context["lang"] = self.request.GET.get("lang")
        context["tags"] = self.request.GET.get("tags")
        if context["lang"]:
            context["searchform"].fields["dataset"].queryset = context["searchform"].fields["dataset"].queryset.filter(signlanguage__language_code_3char=context["lang"])
        context["datasets"] = self.request.GET.getlist("dataset")
        context["first_letters"] = Gloss.objects.filter(dataset__is_public=True, published=True)\
            .annotate(first_letters=Substr(Upper('idgloss'), 1, 1)).order_by('first_letters')\
            .values_list('first_letters').distinct()
        context['lexicons'] = Dataset.objects.filter(is_public=True)
        return context

    def get_queryset(self):
        # Get queryset
        qs = super(TranslationListPublicView, self).get_queryset()
        get = self.request.GET

        # Exclude datasets that are not public.
        qs = qs.exclude(dataset__is_public=False)
        # Exclude glosses that are not 'published'.
        qs = qs.exclude(published=False)

        if 'lang' in get and get['lang'] != '' and get['lang'] != 'all':
            signlang = get.get('lang')
            qs = qs.filter(dataset__signlanguage__language_code_3char=signlang)

        # Search for multiple datasets (if provided)
        vals = get.getlist('dataset', [])
        if vals != []:
            qs = qs.filter(dataset__in=vals)

        if 'gloss' in get and get['gloss'] != '':
            val = get['gloss']
            # Filters
            qs = qs.filter(Q(idgloss__istartswith=val))
        if 'keyword' in get and get['keyword'] != '':
            val = get['keyword']
            # Filters
            qs = qs.filter(translation__keyword__text__istartswith=val)

        # START ISOF
        # From class GlossListView(ListView) in adminviews.py
        if 'tags' in get and get['tags'] != '':
            vals = get.getlist('tags')

            tags = []
            for t in vals:
                tags.extend(Tag.objects.filter(pk=t))

            # search is an implicit AND so intersection
            tqs = TaggedItem.objects.get_intersection_by_model(Gloss, tags)

            # intersection
            qs = qs & tqs

            # print "J :", len(qs)
        # END ISOF


        qs = qs.distinct()

        # Set order according to GET field 'order'
        if 'order' in get:
            qs = qs.order_by(get['order'])
        else:
            qs = qs.order_by('idgloss')

        qs = qs.select_related('dataset')
        # Prefetching translation and dataset objects for glosses to minimize the amount of database queries.
        qs = qs.prefetch_related(Prefetch('glosstranslations_set'),
                                 Prefetch('glosstranslations_set__language'),
                                 # Make sure we only show GlossVideos that have 'is_public=True'
                                 Prefetch('glossvideo_set', queryset=GlossVideo.objects.filter(is_public=True)))
        return qs

class TranslationListPublicView_v0(ListView):
    model = Gloss
    template_name = 'dictionary/public_translation_list.html'
    # template_name = 'translation/public_translation_list.html'
    paginate_by = 20

    def get_queryset(self):
        # Get queryset
        qs = super(TranslationListPublicView, self).get_queryset()
        get = self.request.GET

        # Exclude datasets that are not public.
        qs = qs.exclude(dataset__is_public=False)
        # Exclude glosses that are not 'published'.
        qs = qs.exclude(published=False)

        if 'lang' in get and get['lang'] != '' and get['lang'] != 'all':
            signlang = get.get('lang')
            qs = qs.filter(dataset__signlanguage__language_code_3char=signlang)

        # Search for multiple datasets (if provided)
        vals = get.getlist('dataset', [])
        if vals != []:
            qs = qs.filter(dataset__in=vals)

        if 'gloss' in get and get['gloss'] != '':
            val = get['gloss']
            # Filters
            # qs = qs.filter(Q(idgloss__istartswith=val))
            qs = qs.filter(Q(idgloss__istartswith=val) | Q(translation__keyword__text__istartswith=val))
        if 'keyword' in get and get['keyword'] != '':
            val = get['keyword']
            # Filters
            # qs = qs.filter(translation__keyword__text__istartswith=val)
            qs = qs.filter(Q(idgloss__istartswith=val) | Q(translation__keyword__text__istartswith=val))

        # ISOF test
        category = get.get('tags', 'Alla')

        # Filters
        # qs = qs.filter(Q(idgloss__istartswith=val) | Q(translation__keyword__text__istartswith=val)
                       # | Q(idgloss_en__icontains=val) # idgloss_en not shown in results, therefore removed.
                       # )

        # From class GlossListView(ListView) in adminviews.py
        if 'tags' in get and get['tags'] != '':
            vals = get.getlist('tags')

            tags = []
            for t in vals:
                tags.extend(Tag.objects.filter(pk=t))

            # search is an implicit AND so intersection
            tqs = TaggedItem.objects.get_intersection_by_model(Gloss, tags)

            # intersection
            qs = qs & tqs

            # print "J :", len(qs)


        qs = qs.distinct()

        # Set order according to GET field 'order'
        if 'order' in get:
            qs = qs.order_by(get['order'])
        else:
            qs = qs.order_by('idgloss')

        qs = qs.select_related('dataset')
        # Prefetching translation and dataset objects for glosses to minimize the amount of database queries.
        qs = qs.prefetch_related(Prefetch('glosstranslations_set'),
                                 Prefetch('glosstranslations_set__language'),
                                 # Make sure we only show GlossVideos that have 'is_public=True'
                                 Prefetch('glossvideo_set', queryset=GlossVideo.objects.filter(is_public=True)))
        return qs

class TranslationDetailPublicView(DetailView):
    model = Gloss
    #template_name = 'dictionary/public_gloss_detail.html'
    template_name = 'dictionary/public_translation_detail_v1.html'
    #template_name = 'translation/public_translation_detail.html'
    context_object_name = 'gloss'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TranslationDetailPublicView, self).get_context_data(**kwargs)
        #context['computer'] = Configuration.computer
        gloss = context["gloss"]
        context['translation_languages_and_translations'] = gloss.get_translations_for_translation_languages()
        # GlossRelations for this gloss
        context['glossrelations'] = GlossRelation.objects.filter(source=gloss)
        context['glossrelations_reverse'] = GlossRelation.objects.filter(target=gloss)

        # Create a meta description for the gloss.
        context["metadesc"] = "{glosstxt}: {idgloss} [{lexicon}] / ".format(
            glosstxt=_("Gloss"), idgloss=gloss, lexicon=gloss.dataset.public_name)
        for x in context['translation_languages_and_translations']:
            if x[1]:  # Show language name only if it has translations.
                context["metadesc"] += "{lang}: {trans} / ".format(lang=str(x[0]), trans=str(x[1]))
        context["metadesc"] += "{langtxt}: {lang} / {videotxt}: {videocount} / {notestxt}: {notes}".format(
            langtxt=_("Sign language"), lang=gloss.dataset.signlanguage, videotxt=_("Videos"),
            videocount=gloss.glossvideo_set.all().count(), notestxt=_("Notes"), notes=gloss.notes)
        try:
            context["first_video"] = gloss.glossvideo_set.first()
        except (AttributeError, ValueError):
            context["first_video"] = None
        # Create og:image url for the gloss if the first glossvideo has a posterfile.
        try:
            context["ogimage"] = context["first_video"].posterfile.url
        except (AttributeError, ValueError):
            context["ogimage"] = static('img/signbank_logo_ympyra1_sininen-compressor.png')

        return context

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(published=True)
        # Make sure we only show GlossVideos that have 'is_public=True'
        return qs.prefetch_related(Prefetch('glossvideo_set', queryset=GlossVideo.objects.filter(is_public=True)))


class TranslationDetailPublicView_v0(DetailView):
    model = Gloss
    template_name = 'dictionary/public_translation_detail.html'
    # template_name = 'translation/public_translation_detail.html'
    context_object_name = 'gloss'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TranslationDetailPublicView, self).get_context_data(**kwargs)
        context['computer'] = Configuration.computer
        context['translation_languages_and_translations'] = context['gloss'].get_translations_for_translation_languages()
        # GlossRelations for this gloss
        context['glossrelations'] = GlossRelation.objects.filter(source=context['gloss'])
        context['glossrelations_reverse'] = GlossRelation.objects.filter(target=context['gloss'])
        return context

