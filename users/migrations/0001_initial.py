# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=500, verbose_name=b'\xd0\x97\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('description', models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('active_icon', models.ImageField(upload_to=b'uploads/Achievement/', verbose_name=b'\xd0\x98\xd0\xba\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb0 \xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('inactive_icon', models.ImageField(upload_to=b'uploads/Achievement/', verbose_name=b'\xd0\x98\xd0\xba\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb0 \xd0\xbd\xd0\xb5 \xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'\xd0\xad\xd0\xbb\xd0\xb5\xd0\xba\xd1\x82\xd1\x80\xd0\xbe\xd0\xbd\xd0\xbd\xd0\xb0\xd1\x8f \xd0\xbf\xd0\xbe\xd1\x87\xd1\x82\xd0\xb0', db_index=True)),
                ('username', models.CharField(unique=True, max_length=255, verbose_name=b'\xd0\x9d\xd0\xb8\xd0\xba')),
                ('avatar', models.ImageField(upload_to=b'images/%Y/%m/%d', null=True, verbose_name=b'\xd0\x90\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb0\xd1\x80', blank=True)),
                ('first_name', models.CharField(max_length=255, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f', blank=True)),
                ('last_name', models.CharField(max_length=255, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f', blank=True)),
                ('date_of_birth', models.DateField(null=True, verbose_name=b'\xd0\x94\xd0\xb5\xd0\xbd\xd1\x8c \xd1\x80\xd0\xbe\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserAchievement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.TextField(verbose_name='note', blank=True)),
                ('achievement', models.ForeignKey(verbose_name='achievement', to='users.Achievement')),
                ('user', models.ForeignKey(verbose_name='user', to='users.User')),
            ],
            options={
                'verbose_name': 'user achievement',
                'verbose_name_plural': 'user achievements',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='userachievement',
            unique_together=set([('user', 'achievement')]),
        ),
        migrations.AddField(
            model_name='user',
            name='achievements',
            field=models.ManyToManyField(to='users.Achievement', verbose_name=b'\xd0\x97\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', through='users.UserAchievement'),
            preserve_default=True,
        ),
    ]
