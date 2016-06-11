# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_remove_tournamentresult_games'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='tournament',
            field=models.ForeignKey(related_name='games', to='tracker.Tournament', null=True),
        ),
        migrations.AlterField(
            model_name='showing',
            name='teammates',
            field=models.ManyToManyField(related_name='teammates_rel_+', null=True, to='tracker.Showing'),
        ),
    ]
