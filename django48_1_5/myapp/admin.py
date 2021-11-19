from django.contrib import admin
from .models import Bot, Game, Player


# Register your models here.

class BotAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'level', 'total_games', 'total_win','total_lose','total_tie','win_rate','show_image_html']
    list_filter = ['level']

class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'player', 'bot', 'status', 'created']
    list_filter = ['player', 'bot']


admin.site.register(Bot, BotAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Player)