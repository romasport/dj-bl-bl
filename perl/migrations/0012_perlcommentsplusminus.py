# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perl', '0011_auto_20141218_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerlCommentsPlusMinus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('golos', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'perlcommentsplusminus',
            },
            bases=(models.Model,),
        ),
    ]
