from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    def to_dct(self):
        return {
            "id": self.id,
            "name": self.name
        }

class User(models.Model):
    nickname = models.CharField(max_length=30)
    group = models.ForeignKey(Group, related_name="users")
    description = models.TextField(blank=True)

    def __str__(self):
        return "{nickname} ({group})".format(nickname=self.nickname, group=self.group.name)

    def to_dct(self):
        res = {}
        res["id"] = self.id
        res["group"] = self.group.to_dct()
        res["nickname"] = self.nickname
        res["description"] = self.description
        res["prizes"] = {p.id: p.to_dct() for p in self.prizes}
        res["showings"] = [s.to_dct() for s in self.showings.all()]
        return res
