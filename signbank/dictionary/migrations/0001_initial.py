# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding model 'Translation'
        db.create_table('dictionary_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('gloss', self.gf('django.db.models.fields.related.ForeignKey')
             (to=orm['dictionary.Gloss'])),
            ('translation', self.gf('django.db.models.fields.related.ForeignKey')(
                to=orm['dictionary.Keyword'])),
        ))
        db.send_create_signal('dictionary', ['Translation'])

        # Adding model 'Keyword'
        db.create_table('dictionary_keyword', (
            ('id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')
             (max_length=50)),
        ))
        db.send_create_signal('dictionary', ['Keyword'])

        # Adding model 'Definition'
        db.create_table('dictionary_definition', (
            ('id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('gloss', self.gf('django.db.models.fields.related.ForeignKey')
             (to=orm['dictionary.Gloss'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('role', self.gf('django.db.models.fields.CharField')
             (max_length=20)),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('dictionary', ['Definition'])

        # Adding model 'Gloss'
        db.create_table('dictionary_gloss', (
            ('id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('idgloss', self.gf('django.db.models.fields.CharField')
             (max_length=50)),
            ('annotation_idgloss', self.gf('django.db.models.fields.CharField')(
                max_length=30, blank=True)),
            ('alternate', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('angcongtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('animalstf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('arithmetictf', self.gf('django.db.models.fields.NullBooleanField')(
                null=True, blank=True)),
            ('artstf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('aslgloss', self.gf('django.db.models.fields.CharField')
             (max_length=50, blank=True)),
            ('asloantf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('asltf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('auslextf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('begindirtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('blend', self.gf('django.db.models.fields.CharField')
             (max_length=100, null=True, blank=True)),
            ('blendtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('bodyloctf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('bodyprtstf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('BookProb', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('bslgloss', self.gf('django.db.models.fields.CharField')
             (max_length=50, blank=True)),
            ('bslloantf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('bsltf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('carstf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('catholictf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('cathschtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('citiestf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('clothingtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('colorstf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('comp', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('compound', self.gf('django.db.models.fields.CharField')
             (max_length=100, blank=True)),
            ('comptf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('cookingtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('CorrectionsAdditionsComments', self.gf(
                'django.db.models.fields.TextField')(null=True, blank=True)),
            ('crudetf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('daystf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('deaftf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('dirtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('handedness', self.gf('django.db.models.fields.CharField')
             (max_length=10, blank=True)),
            ('domhndsh', self.gf('django.db.models.fields.CharField')
             (max_length=5, blank=True)),
            ('subhndsh', self.gf('django.db.models.fields.CharField')
             (max_length=5, null=True, blank=True)),
            ('domonly', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('twohand', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('doublehnd', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('locprim', self.gf('django.db.models.fields.IntegerField')
             (null=True, blank=True)),
            ('locsecond', self.gf('django.db.models.fields.IntegerField')
             (null=True, blank=True)),
            ('doubtlextf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('drinkstf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('eductf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('enddirtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('familytf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('feeltf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('fingersptf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('foodstf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('furntf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('general', self.gf('django.db.models.fields.TextField')
             (null=True, blank=True)),
            ('gensigntf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('govtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('groomtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('healthtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('inCD', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('inWeb', self.gf('django.db.models.fields.NullBooleanField')
             (default=False, null=True)),
            ('InMainBook', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('InSuppBook', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('InMedLex', self.gf('django.db.models.fields.NullBooleanField')
             (default=False, null=True)),
            ('isNew', self.gf('django.db.models.fields.NullBooleanField')
             (default=False, null=True)),
            ('inittext', self.gf('django.db.models.fields.CharField')
             (max_length='50', blank=True)),
            ('inittf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('judgetf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('jwtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('langactstf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('lawtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('locdirtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('marginaltf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('materialstf', self.gf('django.db.models.fields.NullBooleanField')(
                null=True, blank=True)),
            ('metalgtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('mindtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('moneytf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('morph', self.gf('django.db.models.fields.CharField')
             (max_length=50, blank=True)),
            ('naturetf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('NotBkDBOnly', self.gf('django.db.models.fields.NullBooleanField')(
                null=True, blank=True)),
            ('numbertf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('obscuretf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('obsoletetf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('onehand', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('opaquetf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('ordertf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('orienttf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('otherreltf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('Palm_orientation', self.gf('django.db.models.fields.CharField')
             (max_length=10, blank=True)),
            ('para', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('peopletf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('physicalactstf', self.gf('django.db.models.fields.NullBooleanField')(
                null=True, blank=True)),
            ('propernametf', self.gf('django.db.models.fields.NullBooleanField')(
                null=True, blank=True)),
            ('qualitytf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('quantitytf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('queries', self.gf('django.db.models.fields.TextField')
             (null=True, blank=True)),
            ('questsigntf', self.gf('django.db.models.fields.NullBooleanField')(
                null=True, blank=True)),
            ('recreationtf', self.gf('django.db.models.fields.NullBooleanField')(
                null=True, blank=True)),
            ('reglextf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('religiontf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('restricttf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('roomstf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('saluttf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('sedefinetf', self.gf('django.db.models.fields.TextField')
             (null=True, blank=True)),
            ('segloss', self.gf('django.db.models.fields.CharField')
             (max_length=50, blank=True)),
            ('sensestf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('seonlytf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('setf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('sextf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('shapestf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('shoppingtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('SpecialCore', self.gf('django.db.models.fields.TextField')
             (null=True, blank=True)),
            ('sporttf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('stateschtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('sthtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('sym', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('techtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('telecomtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('timetf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('tjspeculate', self.gf('django.db.models.fields.TextField')
             (null=True, blank=True)),
            ('transltf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('transptf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('traveltf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('utensilstf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('varlextf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('tastf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('victf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('watf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('satf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('qldtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('nswtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('nthtf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('weathertf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('worktf', self.gf('django.db.models.fields.NullBooleanField')
             (null=True, blank=True)),
            ('sense', self.gf('django.db.models.fields.IntegerField')
             (null=True, blank=True)),
            ('sn', self.gf('django.db.models.fields.IntegerField')
             (null=True, blank=True)),
            ('StemSN', self.gf('django.db.models.fields.IntegerField')
             (null=True, blank=True)),
        ))
        db.send_create_signal('dictionary', ['Gloss'])

        # Adding model 'Relation'
        db.create_table('dictionary_relation', (
            ('id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')
             (related_name='relation_sources', to=orm['dictionary.Gloss'])),
            ('target', self.gf('django.db.models.fields.related.ForeignKey')
             (related_name='relation_targets', to=orm['dictionary.Gloss'])),
            ('role', self.gf('django.db.models.fields.CharField')
             (max_length=20)),
        ))
        db.send_create_signal('dictionary', ['Relation'])

    def backwards(self, orm):

        # Deleting model 'Translation'
        db.delete_table('dictionary_translation')

        # Deleting model 'Keyword'
        db.delete_table('dictionary_keyword')

        # Deleting model 'Definition'
        db.delete_table('dictionary_definition')

        # Deleting model 'Gloss'
        db.delete_table('dictionary_gloss')

        # Deleting model 'Relation'
        db.delete_table('dictionary_relation')

    models = {
        'dictionary.definition': {
            'Meta': {'object_name': 'Definition'},
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'gloss': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dictionary.Gloss']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'dictionary.gloss': {
            'BookProb': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'CorrectionsAdditionsComments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'InMainBook': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'InMedLex': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True'}),
            'InSuppBook': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Gloss'},
            'NotBkDBOnly': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Palm_orientation': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'SpecialCore': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'StemSN': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'alternate': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'angcongtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'animalstf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'annotation_idgloss': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'arithmetictf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'artstf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'aslgloss': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'asloantf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'asltf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'auslextf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'begindirtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'blend': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'blendtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'bodyloctf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'bodyprtstf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'bslgloss': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'bslloantf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'bsltf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'carstf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'catholictf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'cathschtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'citiestf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'clothingtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'colorstf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'comp': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'compound': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'comptf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'cookingtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'crudetf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'daystf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'deaftf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'dirtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'domhndsh': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'domonly': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'doublehnd': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'doubtlextf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'drinkstf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'eductf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'enddirtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'familytf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'feeltf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'fingersptf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'foodstf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'furntf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'general': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'gensigntf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'govtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'groomtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'handedness': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'healthtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idgloss': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'inCD': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'inWeb': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True'}),
            'inittext': ('django.db.models.fields.CharField', [], {'max_length': "'50'", 'blank': 'True'}),
            'inittf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'isNew': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True'}),
            'judgetf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'jwtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'langactstf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'lawtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'locdirtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'locprim': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'locsecond': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'marginaltf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'materialstf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'metalgtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'mindtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'moneytf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'morph': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'naturetf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'nswtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'nthtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'numbertf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'obscuretf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'obsoletetf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'onehand': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'opaquetf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'ordertf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'orienttf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'otherreltf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'para': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'peopletf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'physicalactstf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'propernametf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'qldtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'qualitytf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'quantitytf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'queries': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'questsigntf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'recreationtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'reglextf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'religiontf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'restricttf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'roomstf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'saluttf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'satf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'sedefinetf': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'segloss': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'sense': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sensestf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'seonlytf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'setf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'sextf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'shapestf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'shoppingtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'sn': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sporttf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'stateschtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'sthtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'subhndsh': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'sym': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'tastf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'techtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'telecomtf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'timetf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'tjspeculate': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'transltf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'transptf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'traveltf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'twohand': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'utensilstf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'varlextf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'victf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'watf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'weathertf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'worktf': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'dictionary.keyword': {
            'Meta': {'object_name': 'Keyword'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'dictionary.relation': {
            'Meta': {'object_name': 'Relation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'relation_sources'", 'to': "orm['dictionary.Gloss']"}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'relation_targets'", 'to': "orm['dictionary.Gloss']"})
        },
        'dictionary.translation': {
            'Meta': {'object_name': 'Translation'},
            'gloss': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dictionary.Gloss']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'translation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dictionary.Keyword']"})
        }
    }

    complete_apps = ['dictionary']
