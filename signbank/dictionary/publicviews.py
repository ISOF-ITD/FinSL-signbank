# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q, Prefetch
from django.db.models.functions import Substr, Upper
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.translation import ugettext as _
from django.views.decorators.cache import cache_page
from django.shortcuts import get_object_or_404

from .models import Gloss, Translation, GlossTranslations, SignLanguage, Dataset, GlossRelation, Keyword
from .models import Gloss, Dataset, SignLanguage, GlossRelation, Translation, GlossTranslations, Keyword
from ..video.models import GlossVideo
from .forms import GlossPublicSearchForm
from .adminviews import serialize_glosses

# ISOF Per
from tagging.models import Tag, TaggedItem

# autocomplete
# from dal import autocomplete
from django.views.generic.edit import FormView
import json
from django.http import HttpResponse

# *code in view which returns json data *
class TranslationAutoCompleteView(FormView):
    def get(self,request,*args,**kwargs):
        data = request.GET
        name = data.get("term")
        if name:
            # glosses = Gloss.objects.filter(idgloss__istartswith = name)
            translations = Keyword.objects.filter(text__istartswith = name)
        else:
            translations = Keyword.objects.all()
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
    template_name = 'dictionary/public_translation_list.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TranslationListPublicView, self).get_context_data(**kwargs)
        context["searchform"] = GlossPublicSearchForm(self.request.GET)
        context["signlanguages"] = SignLanguage.objects.filter(id__in=[x.signlanguage.id for x in Dataset.objects.filter(is_public=True)])
        context["lang"] = self.request.GET.get("lang")
        if context["lang"]:
            context["searchform"].fields["dataset"].queryset = context["searchform"].fields["dataset"].queryset.filter(signlanguage__language_code_3char=context["lang"])
        context["first_letters"] = Gloss.objects.filter(dataset__is_public=True, published=True)\
            .annotate(first_letters=Substr(Upper('idgloss'), 1, 1)).order_by('first_letters')\
            .values_list('first_letters').distinct()

        # ISOF Per
        # tags_list = Tag.objects.filter(approved=0).order_by('-date')[:30]
        tag_list = Tag.objects.all()
        context["tags"] = tag_list
        # application_root = applicationRoot(self.request)
        # context["application_root"] = application_root
        # populate_tags_for_object_list(context['object_list'], model=self.object_list.model)

        # context['gloss_choices'] = Gloss.objects.filter(dataset=self.request.GET.get('dataset'))
        context['gloss_choices'] = Gloss.objects.all()

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

        if 'search' in get and get['search'] != '':
            val = get['search']

            # ISOF test
            category = get.get('tags', 'Alla')

            # Filters
            qs = qs.filter(Q(idgloss__istartswith=val) | Q(translation__keyword__text__istartswith=val)
                           # | Q(idgloss_en__icontains=val) # idgloss_en not shown in results, therefore removed.
                           )

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

        # If needed set used translation_lang
        # translation_lang = get_language()
        translation_lang = 'sv'

        # Prefetching translation and dataset objects for glosses to minimize the amount of database queries.
        qs = qs.prefetch_related(Prefetch('translation_set', queryset=Translation.objects.filter(
            language__language_code_2char__iexact=translation_lang).select_related('keyword')),
                                 Prefetch('glosstranslations_set', queryset=GlossTranslations.objects.filter(
                                     language__language_code_2char__iexact=translation_lang)),
                                 Prefetch('dataset'),
                                 # Ordering by version to get the first versions posterfile.
                                 Prefetch('glossvideo_set', queryset=GlossVideo.objects.all().order_by('version')))
        return qs

class GlossListPublicView(ListView):
    model = Gloss
    template_name = 'dictionary/public_gloss_list.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(GlossListPublicView, self).get_context_data(**kwargs)
        context["searchform"] = GlossPublicSearchForm(self.request.GET)
        context["signlanguages"] = SignLanguage.objects.filter(dataset__is_public=True).distinct()
        context["signlanguage_count"] = context["signlanguages"].count()
        context["lang"] = self.request.GET.get("lang")
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
        qs = super(GlossListPublicView, self).get_queryset()
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


class GlossDetailPublicView(DetailView):
    model = Gloss
    template_name = 'dictionary/public_gloss_detail.html'
    context_object_name = 'gloss'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(GlossDetailPublicView, self).get_context_data(**kwargs)
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
        # Create og:image url for the gloss if the first glossvideo has a posterfile.
        try:
            context["ogimage"] = gloss.glossvideo_set.first().posterfile.url
        except (AttributeError, ValueError):
            context["ogimage"] = static('img/signbank_logo_ympyra1_sininen-compressor.png')

        return context

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(published=True)
        # Make sure we only show GlossVideos that have 'is_public=True'
        return qs.prefetch_related(Prefetch('glossvideo_set', queryset=GlossVideo.objects.filter(is_public=True)))


class TranslationDetailPublicView(DetailView):
    model = Gloss
    template_name = 'dictionary/public_translation_detail.html'
    context_object_name = 'gloss'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TranslationDetailPublicView, self).get_context_data(**kwargs)
        context['translation_languages_and_translations'] = context['gloss'].get_translations_for_translation_languages()
        # GlossRelations for this gloss
        context['glossrelations'] = GlossRelation.objects.filter(source=context['gloss'])
        context['glossrelations_reverse'] = GlossRelation.objects.filter(target=context['gloss'])
        return context

@cache_page(60 * 15)
def public_gloss_list_xml(self, dataset_id):
    """Return ELAN schema valid XML of public glosses and their translations."""
    # http://www.mpi.nl/tools/elan/EAFv2.8.xsd
    dataset = get_object_or_404(Dataset, id=dataset_id, is_public=True)
    return serialize_glosses(dataset, Gloss.objects.filter(dataset=dataset, published=True).prefetch_related(
        Prefetch('translation_set', queryset=Translation.objects.filter(gloss__dataset=dataset)
                 .select_related('keyword', 'language')),
        Prefetch('glosstranslations_set', queryset=GlossTranslations.objects
                 .filter(gloss__dataset=dataset).select_related('language'))))
