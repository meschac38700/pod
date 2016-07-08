# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pods', '0008_auto_20160706_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pod',
            name='main_lang',
            field=models.CharField(default='fr', max_length=2, verbose_name='Main language', choices=[('', (('de', 'German'), ('en', 'English'), ('ar', 'Arabic'), ('zh', 'Chinese'), ('es', 'Spanish'), ('fr', 'French'), ('it', 'Italian'), ('ja', 'Japanese'), ('ru', 'Russian'))), ('-----------', (('ab', 'Abkhazian'), ('aa', 'Afar'), ('af', 'Afrikaans'), ('sq', 'Albanian'), ('am', 'Amharic'), ('ar', 'Arabic'), ('an', 'Aragonese'), ('hy', 'Armenian'), ('as', 'Assamese'), ('ay', 'Aymara'), ('az', 'Azerbaijani'), ('ba', 'Bashkir'), ('eu', 'Basque'), ('bn', 'Bengali (Bangla)'), ('dz', 'Bhutani'), ('bh', 'Bihari'), ('bi', 'Bislama'), ('br', 'Breton'), ('bg', 'Bulgarian'), ('my', 'Burmese'), ('be', 'Byelorussian (Belarusian)'), ('km', 'Cambodian'), ('ca', 'Catalan'), ('zh', 'Chinese'), ('co', 'Corsican'), ('hr', 'Croatian'), ('cs', 'Czech'), ('da', 'Danish'), ('nl', 'Dutch'), ('en', 'English'), ('eo', 'Esperanto'), ('et', 'Estonian'), ('fo', 'Faeroese'), ('fa', 'Farsi'), ('fj', 'Fiji'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('gl', 'Galician'), ('gd', 'Gaelic (Scottish)'), ('gv', 'Gaelic (Manx)'), ('ka', 'Georgian'), ('de', 'German'), ('el', 'Greek'), ('kl', 'Greenlandic'), ('gn', 'Guarani'), ('gu', 'Gujarati'), ('ht', 'Haitian Creole'), ('ha', 'Hausa'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hu', 'Hungarian'), ('is', 'Icelandic'), ('io', 'Ido'), ('id', 'Indonesian'), ('ia', 'Interlingua'), ('ie', 'Interlingue'), ('iu', 'Inuktitut'), ('ik', 'Inupiak'), ('ga', 'Irish'), ('it', 'Italian'), ('ja', 'Japanese'), ('jv', 'Javanese'), ('kn', 'Kannada'), ('ks', 'Kashmiri'), ('kk', 'Kazakh'), ('rw', 'Kinyarwanda (Ruanda)'), ('ky', 'Kirghiz'), ('rn', 'Kirundi (Rundi)'), ('ko', 'Korean'), ('ku', 'Kurdish'), ('lo', 'Laothian'), ('la', 'Latin'), ('lv', 'Latvian (Lettish)'), ('li', 'Limburgish ( Limburger)'), ('ln', 'Lingala'), ('lt', 'Lithuanian'), ('mk', 'Macedonian'), ('mg', 'Malagasy'), ('ms', 'Malay'), ('ml', 'Malayalam'), ('mt', 'Maltese'), ('mi', 'Maori'), ('mr', 'Marathi'), ('mo', 'Moldavian'), ('mn', 'Mongolian'), ('na', 'Nauru'), ('ne', 'Nepali'), ('no', 'Norwegian'), ('oc', 'Occitan'), ('or', 'Oriya'), ('om', 'Oromo (Afaan Oromo)'), ('ps', 'Pashto (Pushto)'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pa', 'Punjabi'), ('qu', 'Quechua'), ('rm', 'Rhaeto-Romance'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sm', 'Samoan'), ('sg', 'Sangro'), ('sa', 'Sanskrit'), ('sr', 'Serbian'), ('sh', 'Serbo-Croatian'), ('st', 'Sesotho'), ('tn', 'Setswana'), ('sn', 'Shona'), ('ii', 'Sichuan Yi'), ('sd', 'Sindhi'), ('si', 'Sinhalese'), ('ss', 'Siswati'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('so', 'Somali'), ('es', 'Spanish'), ('su', 'Sundanese'), ('sw', 'Swahili (Kiswahili)'), ('sv', 'Swedish'), ('tl', 'Tagalog'), ('tg', 'Tajik'), ('ta', 'Tamil'), ('tt', 'Tatar'), ('te', 'Telugu'), ('th', 'Thai'), ('bo', 'Tibetan'), ('ti', 'Tigrinya'), ('to', 'Tonga'), ('ts', 'Tsonga'), ('tr', 'Turkish'), ('tk', 'Turkmen'), ('tw', 'Twi'), ('ug', 'Uighur'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('vi', 'Vietnamese'), ('vo', 'Volap\xfck'), ('wa', 'Wallon'), ('cy', 'Welsh'), ('wo', 'Wolof'), ('xh', 'Xhosa'), ('yi', 'Yiddish'), ('yo', 'Yoruba'), ('zu', 'Zulu')))]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trackpods',
            name='lang',
            field=models.CharField(max_length=2, verbose_name='Language', choices=[('', (('de', 'German'), ('en', 'English'), ('ar', 'Arabic'), ('zh', 'Chinese'), ('es', 'Spanish'), ('fr', 'French'), ('it', 'Italian'), ('ja', 'Japanese'), ('ru', 'Russian'))), ('-----------', (('ab', 'Abkhazian'), ('aa', 'Afar'), ('af', 'Afrikaans'), ('sq', 'Albanian'), ('am', 'Amharic'), ('ar', 'Arabic'), ('an', 'Aragonese'), ('hy', 'Armenian'), ('as', 'Assamese'), ('ay', 'Aymara'), ('az', 'Azerbaijani'), ('ba', 'Bashkir'), ('eu', 'Basque'), ('bn', 'Bengali (Bangla)'), ('dz', 'Bhutani'), ('bh', 'Bihari'), ('bi', 'Bislama'), ('br', 'Breton'), ('bg', 'Bulgarian'), ('my', 'Burmese'), ('be', 'Byelorussian (Belarusian)'), ('km', 'Cambodian'), ('ca', 'Catalan'), ('zh', 'Chinese'), ('co', 'Corsican'), ('hr', 'Croatian'), ('cs', 'Czech'), ('da', 'Danish'), ('nl', 'Dutch'), ('en', 'English'), ('eo', 'Esperanto'), ('et', 'Estonian'), ('fo', 'Faeroese'), ('fa', 'Farsi'), ('fj', 'Fiji'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('gl', 'Galician'), ('gd', 'Gaelic (Scottish)'), ('gv', 'Gaelic (Manx)'), ('ka', 'Georgian'), ('de', 'German'), ('el', 'Greek'), ('kl', 'Greenlandic'), ('gn', 'Guarani'), ('gu', 'Gujarati'), ('ht', 'Haitian Creole'), ('ha', 'Hausa'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hu', 'Hungarian'), ('is', 'Icelandic'), ('io', 'Ido'), ('id', 'Indonesian'), ('ia', 'Interlingua'), ('ie', 'Interlingue'), ('iu', 'Inuktitut'), ('ik', 'Inupiak'), ('ga', 'Irish'), ('it', 'Italian'), ('ja', 'Japanese'), ('jv', 'Javanese'), ('kn', 'Kannada'), ('ks', 'Kashmiri'), ('kk', 'Kazakh'), ('rw', 'Kinyarwanda (Ruanda)'), ('ky', 'Kirghiz'), ('rn', 'Kirundi (Rundi)'), ('ko', 'Korean'), ('ku', 'Kurdish'), ('lo', 'Laothian'), ('la', 'Latin'), ('lv', 'Latvian (Lettish)'), ('li', 'Limburgish ( Limburger)'), ('ln', 'Lingala'), ('lt', 'Lithuanian'), ('mk', 'Macedonian'), ('mg', 'Malagasy'), ('ms', 'Malay'), ('ml', 'Malayalam'), ('mt', 'Maltese'), ('mi', 'Maori'), ('mr', 'Marathi'), ('mo', 'Moldavian'), ('mn', 'Mongolian'), ('na', 'Nauru'), ('ne', 'Nepali'), ('no', 'Norwegian'), ('oc', 'Occitan'), ('or', 'Oriya'), ('om', 'Oromo (Afaan Oromo)'), ('ps', 'Pashto (Pushto)'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pa', 'Punjabi'), ('qu', 'Quechua'), ('rm', 'Rhaeto-Romance'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sm', 'Samoan'), ('sg', 'Sangro'), ('sa', 'Sanskrit'), ('sr', 'Serbian'), ('sh', 'Serbo-Croatian'), ('st', 'Sesotho'), ('tn', 'Setswana'), ('sn', 'Shona'), ('ii', 'Sichuan Yi'), ('sd', 'Sindhi'), ('si', 'Sinhalese'), ('ss', 'Siswati'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('so', 'Somali'), ('es', 'Spanish'), ('su', 'Sundanese'), ('sw', 'Swahili (Kiswahili)'), ('sv', 'Swedish'), ('tl', 'Tagalog'), ('tg', 'Tajik'), ('ta', 'Tamil'), ('tt', 'Tatar'), ('te', 'Telugu'), ('th', 'Thai'), ('bo', 'Tibetan'), ('ti', 'Tigrinya'), ('to', 'Tonga'), ('ts', 'Tsonga'), ('tr', 'Turkish'), ('tk', 'Turkmen'), ('tw', 'Twi'), ('ug', 'Uighur'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('vi', 'Vietnamese'), ('vo', 'Volap\xfck'), ('wa', 'Wallon'), ('cy', 'Welsh'), ('wo', 'Wolof'), ('xh', 'Xhosa'), ('yi', 'Yiddish'), ('yo', 'Yoruba'), ('zu', 'Zulu')))]),
            preserve_default=True,
        ),
    ]
