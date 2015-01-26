# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_news_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_descreption',
            field=models.TextField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='news_keywords',
            field=models.TextField(default='', help_text=b'\xd0\x9a\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xb2\xd1\x8b\xd0\xb5 \xd1\x81\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xb0 \xd1\x87\xd0\xb5\xd1\x80\xd0\xb5\xd0\xb7 \xd0\xb7\xd0\xb0\xd0\xbf\xd1\x8f\xd1\x82\xd1\x83\xd1\x8e', blank=True),
            preserve_default=False,
        ),
    ]
