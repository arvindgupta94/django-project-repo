# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pollsnew', '0010_auto_20160124_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date created'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 26, 3, 28, 44, 540000, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
