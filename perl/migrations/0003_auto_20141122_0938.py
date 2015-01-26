# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perl', '0002_perl_perl_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perl',
            name='perl_img',
            field=models.ImageField(help_text=b'\xd0\x9a\xd0\xb0\xd1\x80\xd1\x82\xd0\xb8\xd0\xbd\xd0\xba\xd0\xb0 \xd0\xbf\xd0\xb5\xd1\x80\xd0\xbb\xd0\xb0', upload_to=b'perlimg', null=True, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb0\xd0\xbb\xd1\x8c\xd0\xb1\xd0\xbe\xd0\xbc\xd0\xb0'),
            preserve_default=True,
        ),
    ]
