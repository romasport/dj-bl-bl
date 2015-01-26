# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perl', '0008_comments_comments_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comments_pub',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
