# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from django.utils.safestring import mark_safe
from string import Template

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

    def map_tag(self):
        values = {
            'lat': str(self.lat),
            'lng': str(self.lng)
        }
        map_template = """
            <link rel="stylesheet" href="https://unpkg.com/leaflet@1.2.0/dist/leaflet.css" />
            <script src="https://unpkg.com/leaflet@1.3.1/dist/leaflet.js"></script>
            <script type="text/javascript" src="https://unpkg.com/leaflet.vectorgrid@1.2.0"></script>
            <div id="socken_map" style="width: 100%; height: 400px;"></div>
            <script type="text/javascript">
                var map = L.map("socken_map").setView([${lat}, ${lng}], 8); // Skapar en karta
                L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {attribution: "&copy; <a href='http://osm.org/copyright'>OpenStreetMap</a> contributors"}).addTo(map);

                var layer = 'SockenStad_ExtGranskning-clipped:SockenStad_ExtGranskn_v1.0_clipped'
                var isoftilesUrl = 'https://oden.isof.se/geoserver/gwc/service/wmts?REQUEST=GetTile&SERVICE=WMTS&VERSION=1.0.0&LAYER=' + layer + '&STYLE=&TILEMATRIX=EPSG:900913:{z}&TILEMATRIXSET=EPSG:900913&FORMAT=application/x-protobuf;type=mapbox-vector&TILECOL={x}&TILEROW={y}'
                var isofVectorTileOptions = {
                    rendererFactory: L.canvas.tile,
                    maxZoom: 14
                };
                var isofPbfLayer = L.vectorGrid.protobuf(isoftilesUrl, isofVectorTileOptions).addTo(map);

                var marker = L.marker([${lat}, ${lng}]); // Lägger till en L.marker
                marker.addTo(map);

                map.on('click', function(e) { // Map click handler
                    marker.setLatLng(e.latlng); // Uppdaterar punkten på kartan

                    django.jQuery('#id_lat').val(e.latlng.lat.toFixed(6)); // Skriver e.latlng.lat från punkter var man klickade på kartan till "lat" fältet
                    django.jQuery('#id_lng').val(e.latlng.lng.toFixed(6)); // Skriver e.latlng.lng från punkter var man klickade på kartan till "lng" fältet
                });
            </script>
        """

        template = Template(map_template)

        map_html = template.substitute(values)

        return mark_safe(map_html);

    map_tag.short_description = 'Karta'
    map_tag.allow_tags = True

    class Meta:
        db_table = 'ortnamn_tecken'
        verbose_name = 'Ortnamn-tecken'
        verbose_name_plural = LEVEL1 + 'Ortnamn-tecken'
        # ordering = ['id',]

    def __str__(self):
        return self.ortnamn
