from django.db import models
from django.contrib.auth.models import User
from django.utils.html import  format_html
from PIL import Image
# Create your models here.

class Player(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='upload/player/', null=True, blank=True)
    total_games = models.IntegerField(default=0)
    total_win = models.IntegerField(default=0)
    total_lose = models.IntegerField(default=0)
    total_tie = models.IntegerField(default=0)
    win_rate = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        super(Player, self).save(*args, **kwargs)
        if self.profile_pic:
            imag = Image.open(self.profile_pic.path).resize((512,512))
            imag.save(self.profile_pic.path)
            
    def show_image(self):
        if self.profile_pic:
            return self.profile_pic.url
        else:
            return '/media/upload/player/profile.png'

    def __str__(self):
        return self.user.username



BOT_LEVE_CHOICE =(
    ('BEGINNER', 'Beginner'),
    ('INTERMEDIATE', 'Intermediate'),
    ('ADVANCED', 'Advanced')
)


class  Bot(models.Model):
    name = models.CharField(max_length=100, default="", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='upload/bot/', null=True, blank=True)
    level = models.CharField(max_length =20, null=True, blank=True, choices=BOT_LEVE_CHOICE )
    total_games = models.IntegerField(default=0)
    total_win = models.IntegerField(default=0)
    total_lose = models.IntegerField(default=0)
    total_tie = models.IntegerField(default=0)
    win_rate = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        super(Bot, self).save(*args, **kwargs)
        if self.image:
            imag = Image.open(self.image.path).resize((512,512))
            imag.save(self.image.path)
    

    def show_image_html(self):
        if self.image:
            return format_html('<img src="%s" height="40px" >' % self.image.url)
        else:
            return ''
    
    def show_image(self):
        if self.image:
            return self.image.url
        else:
            return '/media/upload/bot/default_bot.jpg'
    
    def __nonzero__(self):
        return bool(self.image)

    def __str__(self):
        return self.name



WIN_CHOICE =(
    ('WIN', 'Win'),
    ('LOSE', 'Lose'),
    ('TIE', 'Tie')
)

class Game(models.Model):
    player = models.ForeignKey(Player, null=True, blank=True,on_delete=models.CASCADE)
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    player_play = models.CharField(max_length=1)
    status = models.CharField(max_length=5, null=True, blank=True, choices=WIN_CHOICE)
    board1 = models.CharField(max_length=1)
    board2 = models.CharField(max_length=1)
    board3 = models.CharField(max_length=1)
    board4 = models.CharField(max_length=1)
    board5 = models.CharField(max_length=1)
    board6 = models.CharField(max_length=1)
    board7 = models.CharField(max_length=1)
    board8 = models.CharField(max_length=1)
    board9 = models.CharField(max_length=1)

    def __str__(self):
        return str(self.id)

