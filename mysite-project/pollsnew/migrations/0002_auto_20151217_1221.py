# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollsnew', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='hits',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='hits',
            field=models.IntegerField(default=0),
        ),
    ]
