# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments_text', models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd1\x8f')),
            ],
            options={
                'db_table': 'comments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Perl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('perl_title', models.CharField(max_length=200)),
                ('perl_text', models.TextField()),
                ('perl_date', models.DateTimeField()),
                ('perl_likes', models.IntegerField(default=0)),
                ('perl_dontlike', models.IntegerField(default=0)),
                ('perl_slug', models.SlugField(unique=True, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f \xd0\xb4\xd0\xbb\xd1\x8f \xd1\x81\xd1\x81\xd1\x8b\xd0\xbb\xd0\xba\xd0\xb8')),
            ],
            options={
                'db_table': 'perl',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comments',
            name='comments_perl',
            field=models.ForeignKey(to='perl.Perl'),
            preserve_default=True,
        ),
    ]
