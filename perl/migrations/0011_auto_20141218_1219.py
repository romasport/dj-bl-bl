# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perl', '0010_auto_20141217_1101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='comments_rating',
            new_name='comments_minus',
        ),
        migrations.AddField(
            model_name='comments',
            name='comments_pearent',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comments',
            name='comments_plus',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
