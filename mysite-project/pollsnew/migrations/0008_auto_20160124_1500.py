# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pollsnew', '0007_auto_20160124_1459'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserVote',
            new_name='UserData',
        ),
        migrations.AlterField(
            model_name='category',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 24, 9, 30, 28, 762000, tzinfo=utc), verbose_name=b'date created'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 24, 9, 30, 28, 762000, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
