# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perl', '0007_perlplusminus'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comments_userid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
