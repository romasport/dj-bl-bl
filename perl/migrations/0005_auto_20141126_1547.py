# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perl', '0004_auto_20141122_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='perl',
            name='perl_descreption',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perl',
            name='perl_keywords',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
    ]
