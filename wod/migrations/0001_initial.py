# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('warm_up', models.TextField()),
                ('metcon', models.TextField()),
                ('weightlifting', models.TextField()),
                ('strength_accessory', models.TextField()),
            ],
        ),
    ]
