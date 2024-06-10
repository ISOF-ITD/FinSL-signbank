# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from reversion.admin import VersionAdmin

from .models_isof import Ortnamn_tecken


class Ortnamn_teckenAdmin(VersionAdmin):
    # Making sure these fields are not edited in admin
    readonly_fields = ('id','createdate', 'createdby', 'changedate', 'editedby','map_tag',)
    actions = []

    fields = [('id', 'ortnamn'), ('lat', 'lng'), 'forklaring_svenska', 'forklaring_tecken',
            'teckenfilnamn',
             # 'teckenfilnamn2',
             # 'teckenfilnamn3',
              ('createdate', 'createdby', 'changedate', 'editedby'), 'map_tag']

    save_on_top = True
    # save_as = True
    list_display = ['id', 'ortnamn', 'teckenfilnamn']
    # list_display = ['id', 'ortnamn', 'teckenfilnamn', 'teckenfilnamn2', 'teckenfilnamn3']
    search_fields = ['^ortnamn']
    # list_filter = ('dataset', 'published', 'exclude_from_ecv', TagListFilter, )

    def save_model(self, request, obj, form, change):
        if change == True:  # Was the post changed?
            obj.editedby = request.user  # Get the current user and log it as the editor
        else:  # The post might be new
            if getattr(obj, 'createdby', None) is None:  # check if the creator is defined
                obj.createdby = request.user  # If not, set the current user as the creator
        obj.save()  # Save the post.
