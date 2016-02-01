# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pollsnew', '0002_auto_20151217_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 17, 49, 2, 400000, tzinfo=utc), verbose_name=b'date created'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 18, 17, 49, 2, 400000, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
