from django.db import models
from tracker.models.user import User


class Character(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def to_dct(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
    

class Map(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def to_dct(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
    

class Tournament(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ruling = models.CharField(max_length=1, choices=(('1', 'league'), ('2', 'single_elimination'), ('3', 'double_elimination'), ('4', 'other'),))
    registration = models.CharField(max_length=1, choices=(('1', 'open'), ('2', 'qualification'),))
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def to_dct(self):
        res = {}
        res["id"] = self.id
        res["name"] = self.name
        res["ruling"] = self.get_ruling_display()
        res["registration"] = self.get_registration_display()
        res["results"] = {r.position: r.to_dct() for r in self.results.all()}
        res["description"] = self.description
        return res


class Game(models.Model):
    date = models.DateField()
    stage = models.ForeignKey(Map, related_name="games")
    tournament = models.ForeignKey(Tournament, related_name="games", null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return "{s} {i} ({d})".format(i=str(self.id), s=str(self.stage), d=str(self.date))

    def to_dct(self):
        showings = self.showings.all()
        res = {}
        res["id"] = self.id
        res["stage"] = self.stage.id
        res["date"] = self.date
        res["users"] = [showing.user.id for showing in showings]
        res["characters"] = [showing.character.id for showing in showings]
        res["participants"] = {showing.character.id: showing.user.id for showing in showings}
        winners = showings.filter(win=True)
        assert len(winners) == 1 #only duels for now
        res["winner"] = winners[0].user.id
        res["tournament"] = None if self.tournament is None else self.tournament.id
        return res


class Showing(models.Model):
    user = models.ForeignKey(User, related_name="showings")
    character = models.ForeignKey(Character, related_name="showings")
    game = models.ForeignKey(Game, related_name="showings")
    win = models.BooleanField()
    description = models.TextField(blank=True)

    def __str__(self):
        return "{w} by {u} on {g}".format(w="Win" if self.win else "Loss", u=str(self.user), g=str(self.game))

    def to_dct(self):
        res = {}
        res["id"] = self.id
        res["game"] = self.game.to_dct()
        res["user"] = self.user.id
        res["character"] = self.character.to_dct()
        res["win"] = self.win
        res["description"] = self.description
        return res


class TournamentResult(models.Model):
    position = models.IntegerField()
    tournament = models.ForeignKey(Tournament, related_name="results")
    user = models.ForeignKey(User, related_name="tournament_results")
    description = models.TextField(blank=True)

    def __str__(self):
        return "top{p} finish in {t} by {u}".format(p=str(self.position), t=str(self.tournament), u=str(self.user))

    def to_dct(self):
        res = {}
        res["id"] = self.id
        res["position"] = self.position
        res["tournament"] = self.tournament.id
        res["user"] = self.user.to_dct()
        res["prizes"] = {p.id: p.to_dct() for p in self.prizes}
        res["description"] = self.description
        return res


class Prize(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=1, choices=(('1', 'symbolic'), ('2', 'low'), ('3', 'medium'), ('4', 'high'), ('5', 'immeasurable'),))
    owner = models.ForeignKey(User, related_name="prizes")
    achievement = models.ForeignKey(TournamentResult, related_name="prizes")
    tournament = models.ForeignKey(Tournament, related_name="prizes")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name + " for " + str(self.tournament)

    def to_dct(self):
        res = {}
        res["id"] = self.id
        res["name"] = self.name
        res["value"] = self.get_value_display()
        res["owner"] = self.owner.to_dct()
        res["achievment"] = self.achievement.id
        res["tournament"] =  self.tournament.id
        res["description"] = self.description
        return res
