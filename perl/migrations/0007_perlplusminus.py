# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perl', '0006_auto_20141126_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerlPlusMinus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('perl_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('golos', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'perlplusminus',
            },
            bases=(models.Model,),
        ),
    ]
