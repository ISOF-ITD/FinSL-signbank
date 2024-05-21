# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from reversion.admin import VersionAdmin

from .models_isof import Ortnamn_tecken


class Ortnamn_teckenAdmin(VersionAdmin):
    # Making sure these fields are not edited in admin
    readonly_fields = ('createdate', 'createdby', 'changedate', 'editedby',)
    actions = []

    fields = ['id', 'ortnamn', 'forklaring_svenska', 'forklaring_tecken',
            'teckenfilnamn',
              'teckenfilnamn2',
              'teckenfilnamn3',
              ('createdate', 'createdby', 'changedate', 'editedby')]

    save_on_top = True
    # save_as = True
    list_display = ['id', 'ortnamn', 'teckenfilnamn', 'teckenfilnamn2', 'teckenfilnamn3']
    search_fields = ['^ortnamn']
    # list_filter = ('dataset', 'published', 'exclude_from_ecv', TagListFilter, )

