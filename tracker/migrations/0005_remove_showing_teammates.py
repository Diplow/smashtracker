# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20160611_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showing',
            name='teammates',
        ),
    ]
