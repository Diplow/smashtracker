from tracker.models.user import Group, User
from tracker.models.smash import Character, Map, Tournament, Game, Showing, TournamentResult, Prize

from django.contrib import admin

admin.site.register(Group)
admin.site.register(User)
admin.site.register(Character)
admin.site.register(Map)
admin.site.register(Tournament)
admin.site.register(Game)
admin.site.register(Showing)
admin.site.register(TournamentResult)
admin.site.register(Prize)
