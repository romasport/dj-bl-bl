# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('news_title', models.CharField(max_length=200)),
                ('news_text', models.TextField()),
                ('news_date', models.DateTimeField()),
                ('news_slug', models.SlugField(unique=True, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f \xd0\xb4\xd0\xbb\xd1\x8f \xd1\x81\xd1\x81\xd1\x8b\xd0\xbb\xd0\xba\xd0\xb8')),
            ],
            options={
                'db_table': 'news',
            },
            bases=(models.Model,),
        ),
    ]
