# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('level', models.CharField(max_length=1, choices=[(b'0', b'trainee'), (b'1', b'junior'), (b'2', b'senior'), (b'3', b'lead'), (b'4', b'executive')])),
                ('division', models.CharField(max_length=1, choices=[(b'1', b'r&d'), (b'2', b'consulting'), (b'3', b'creative'), (b'4', b'other')])),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('value', models.CharField(max_length=1, choices=[(b'1', b'symbolic'), (b'2', b'low'), (b'3', b'medium'), (b'4', b'high'), (b'5', b'immeasurable')])),
            ],
        ),
        migrations.CreateModel(
            name='Showing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('win', models.BooleanField()),
                ('character', models.ForeignKey(related_name='showings', to='tracker.Character')),
                ('game', models.ForeignKey(related_name='showings', to='tracker.Game')),
                ('teammates', models.ManyToManyField(related_name='teammates_rel_+', to='tracker.Showing')),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('ruling', models.CharField(max_length=1, choices=[(b'1', b'league'), (b'2', b'single_elimination'), (b'3', b'double_elimination'), (b'4', b'other')])),
                ('registration', models.CharField(max_length=1, choices=[(b'1', b'open'), (b'2', b'qualification')])),
            ],
        ),
        migrations.CreateModel(
            name='TournamentResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField()),
                ('games', models.ManyToManyField(to='tracker.Game')),
                ('tournament', models.ForeignKey(related_name='results', to='tracker.Tournament')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=1, choices=[(b'1', b'male'), (b'2', b'female'), (b'3', b'unknown')])),
                ('birthday', models.DateField()),
                ('job', models.ForeignKey(related_name='users', to='tracker.Job')),
            ],
        ),
        migrations.AddField(
            model_name='tournamentresult',
            name='user',
            field=models.ForeignKey(related_name='tournament_results', to='tracker.User'),
        ),
        migrations.AddField(
            model_name='showing',
            name='user',
            field=models.ForeignKey(related_name='showings', to='tracker.User'),
        ),
        migrations.AddField(
            model_name='prize',
            name='achievement',
            field=models.ForeignKey(related_name='prizes', to='tracker.TournamentResult'),
        ),
        migrations.AddField(
            model_name='prize',
            name='owner',
            field=models.ForeignKey(related_name='prizes', to='tracker.User'),
        ),
        migrations.AddField(
            model_name='prize',
            name='tournament',
            field=models.ForeignKey(related_name='prizes', to='tracker.Tournament'),
        ),
        migrations.AddField(
            model_name='game',
            name='stage',
            field=models.ForeignKey(related_name='games', to='tracker.Map'),
        ),
        migrations.AddField(
            model_name='game',
            name='tournament',
            field=models.ForeignKey(related_name='games', to='tracker.Tournament'),
        ),
    ]
