# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pollsnew', '0005_auto_20160123_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.ForeignKey(to='pollsnew.Choice')),
            ],
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='question',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='user',
        ),
        migrations.AlterField(
            model_name='category',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 24, 9, 26, 4, 136000, tzinfo=utc), verbose_name=b'date created'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 24, 9, 26, 4, 136000, tzinfo=utc), verbose_name=b'date published'),
        ),
        migrations.DeleteModel(
            name='UserData',
        ),
        migrations.AddField(
            model_name='uservote',
            name='question',
            field=models.ForeignKey(to='pollsnew.Question'),
        ),
        migrations.AddField(
            model_name='uservote',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
