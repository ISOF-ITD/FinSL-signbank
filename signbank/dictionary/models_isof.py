# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Invisible space used to change default django admin alphabetic order of models
LEVEL1 = u"\u200B"
LEVEL2 = u"\u200B" + u"\u200B"
LEVEL3 = u"\u200B" + u"\u200B" + u"\u200B"
LEVEL4 = u"\u200B" + u"\u200B" + u"\u200B" + u"\u200B"

class Ortnamn_tecken(models.Model):
    """Placenames (ortnamn) with signs

    python3 /home/per/dev/server/teckenlistan/FinSL-signbank/bin/develop.py migrate dictionary 0007 --fake
    """
    # Coordinates
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    # Placename
    ortnamn = models.CharField(max_length=60, blank=True, null=True, verbose_name="Ortnamn på svenska")
    # Swedish placename explanation
    forklaring_svenska = models.TextField(blank=True, null=True, verbose_name="Förklaring svenskt namn")
    # Swedish placename explanation
    forklaring_tecken = models.TextField(blank=True, null=True, verbose_name="Förklaring tecken STS")
    #: File name with relative path to sign file
    teckenfilnamn = models.CharField(max_length=60, blank=True, null=True, verbose_name="Filnamn tecken med sökväg")
    #: File name with relative path to sign file number 2
    teckenfilnamn2 = models.CharField(max_length=60, blank=True, null=True, verbose_name="Filnamn tecken 2 med sökväg")
    #: File name with relative path to sign file number 3
    teckenfilnamn3 = models.CharField(max_length=60, blank=True, null=True, verbose_name="Filnamn tecken 3 med sökväg")

    # Track data changes:
    createdate = models.DateTimeField(auto_now_add=True, verbose_name="Skapad datum")
    changedate = models.DateTimeField(auto_now=True, blank=True, verbose_name="Ändrad datum")
    createdby = models.ForeignKey(User, db_column='createdby', null=True, blank=True, editable=False, on_delete=models.DO_NOTHING,
                             verbose_name="Skapad av")
    editedby = models.ForeignKey(User, db_column='editedby', null=True, blank=True, editable=False, on_delete=models.DO_NOTHING,
                                 related_name='Uppdaterad av+', verbose_name="Uppdaterad av")

    class Meta:
        db_table = 'ortnamn_tecken'
        verbose_name = 'Ortnamn-tecken'
        verbose_name_plural = LEVEL1 + 'Ortnamn-tecken'
        # ordering = ['id',]

    def __str__(self):
        return self.ortnamn
