from django.db import models
from tracker.models.user import User


class Character(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Map(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    ruling = models.CharField(max_length=1, choices=(('1', 'league'), ('2', 'single_elimination'), ('3', 'double_elimination'), ('4', 'other'),))
    registration = models.CharField(max_length=1, choices=(('1', 'open'), ('2', 'qualification'),))

    def __str__(self):
        return self.name


class Game(models.Model):
    date = models.DateField()
    stage = models.ForeignKey(Map, related_name="games")
    tournament = models.ForeignKey(Tournament, related_name="games", null=True)

    def __str__(self):
        return "{s} {i} ({d})".format(i=str(self.id), s=str(self.stage), d=str(self.date))

    def to_es(self):
        showings = self.showings.all()
        res = {}
        res["id"] = self.id
        res["stage"] = self.stage.id
        res["date"] = self.date
        res["users"] = [showing.user.id for showing in showings]
        res["participants"] = {showing.character.id: showing.user.id for showing in showings}
        res["characters"] = [showing.character.id for showing in showings]
        winners = showings.filter(win=True)
        assert len(winners) == 1
        res["winner"] = winners[0].user.id
        res["tournament"] = None if self.tournament is None else self.tournament.id
        return res


class Showing(models.Model):
    user = models.ForeignKey(User, related_name="showings")
    character = models.ForeignKey(Character, related_name="showings")
    game = models.ForeignKey(Game, related_name="showings")
    win = models.BooleanField()

    def __str__(self):
        return "{w} by {u} on {g}".format(w="Win" if self.win else "Loss", u=str(self.user), g=str(self.game))


class TournamentResult(models.Model):
    position = models.IntegerField()
    tournament = models.ForeignKey(Tournament, related_name="results")
    user = models.ForeignKey(User, related_name="tournament_results")

    def __str__(self):
        return "top{p} finish in {t} by {u}".format(p=str(self.position), t=str(self.tournament), u=str(self.user))


class Prize(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    value = models.CharField(max_length=1, choices=(('1', 'symbolic'), ('2', 'low'), ('3', 'medium'), ('4', 'high'), ('5', 'immeasurable'),))
    owner = models.ForeignKey(User, related_name="prizes")
    achievement = models.ForeignKey(TournamentResult, related_name="prizes")
    tournament = models.ForeignKey(Tournament, related_name="prizes")

    def __str__(self):
        return self.name + " for " + str(self.tournament)
