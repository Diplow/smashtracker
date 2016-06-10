from django.db import models
from tracker.models.user import User


class Character(models.Model):
    name = models.CharField(max_length=20)


class Map(models.Model):
    name = models.CharField(max_length=20)


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    format_ = models.CharField(max_length=1, choices=(('1', 'league'), ('2', 'single_elimination'), ('3', 'double_elimination'), ('4', 'other'),))
    registration = models.CharField(max_length=1, choices=(('1', 'open'), ('2', 'qualification'),))


class Game(models.Model):
    date = models.DateField()
    map_ = models.ForeignKey(Map, related_name="games")
    tournament = models.ForeignKey(Tournament, related_name="games")


class Showing(models.Model):
    user = models.ForeignKey(User, related_name="showings")
    character = models.ForeignKey(Character, related_name="showings")
    game = models.ForeignKey(Game, related_name="showings")
    win = models.BooleanField()
    teammates = models.ManyToManyField("self")


class TournamentResult(models.Model):
    position = models.IntegerField()
    tournament = models.ForeignKey(Tournament, related_name="results")
    games = models.ManyToManyField(Game)
    user = models.ForeignKey(User, related_name="tournament_results")


class Prize(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    value = models.CharField(max_length=1, choices=(('1', 'symbolic'), ('2', 'low'), ('3', 'medium'), ('4', 'high'), ('5', 'immeasurable'),))
    owner = ForeignKey(User, related_name="prizes")
    achievement = models.ForeignKey(TournamentResult, related_name="prizes")
    tournament = models.ForeignKey(Tournament, related_name="prizes")
