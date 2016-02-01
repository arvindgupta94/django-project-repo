# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pollsnew', '0009_auto_20160124_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='addedBy',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='addedBy',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='category',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 24, 10, 32, 56, 901000, tzinfo=utc), verbose_name=b'date created'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 24, 10, 32, 56, 901000, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
