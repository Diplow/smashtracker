# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20160611_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showing',
            name='teammates',
            field=models.ManyToManyField(related_name='teammates_rel_+', to='tracker.Showing', blank=True),
        ),
    ]
