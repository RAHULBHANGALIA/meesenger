# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('prjctapp', '0002_auto_20140718_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
