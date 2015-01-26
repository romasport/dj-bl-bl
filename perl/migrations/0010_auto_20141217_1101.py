# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('perl', '0009_comments_comments_pub'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comments_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 17, 8, 1, 36, 122000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='comments_rating',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments_pub',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
