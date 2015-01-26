# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20141126_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_preview',
            field=models.TextField(default='', verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb2\xd1\x8c\xd1\x8e \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xbb\xd0\xb5\xd0\xb2\xd0\xbe\xd0\xb9 \xd0\xba\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb8'),
            preserve_default=False,
        ),
    ]
