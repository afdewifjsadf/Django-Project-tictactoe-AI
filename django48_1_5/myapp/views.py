from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Bot, Player, Game
from .forms import CreateUserForm, PlayerImageForm, UpdateUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.
from django.contrib.auth.decorators import  login_required
from .decorators import unauthenticated_user



def index(request):
    bots = Bot.objects.all().values()
    context = {'bots': json.dumps(list(bots), cls=DjangoJSONEncoder)}
    if request.user.is_authenticated:
        player = request.user.player_set.get()
        context['player'] = player
    return render(request, 'index.html', context)

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Player.objects.create(
                user=user
            )
            messages.success(request, "Accout was created for " + username)
            return redirect('myapp:login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/')

@login_required( login_url='myapp:login')
def profile(request):
    player = request.user.player_set.get()
    games = player.game_set.all()
    paginator = Paginator(games, 15)
    page = request.GET.get('page')
    try:
        games = paginator.page(page)
    except PageNotAnInteger:
        games = paginator.page(1)
    except EmptyPage:
        games = paginator.page(paginator.num_pages())

    context = {'player': player, 'games': games}

    return render(request, 'accounts/profile.html', context)


def accountPage(request):
    player = request.user.player_set.get()
    user = request.user
    form_playerImage = PlayerImageForm(instance=player)
    form_user = UpdateUserForm(instance=user)
    if request.method == 'POST':
        form_playerImage = PlayerImageForm(
            request.POST, request.FILES, instance=player)
        form_user = UpdateUserForm(request.POST, instance=user)
        if form_playerImage.is_valid() and form_user.is_valid():
            form_playerImage.save()
            form_user.save()
            messages.success(request, f'Your account has been updated!')
        return redirect('myapp:index')

    context = {'form_playerImage': form_playerImage, 'form_user': form_user}
    if request.user.is_authenticated:
        player = request.user.player_set.get()
        context['player'] = player
    return render(request, 'accounts/account_setting.html', context)


def createGame(request):
    print(request.POST['bot'])
    if request.user.is_authenticated:
        player = request.user.player_set.get()
        bot = Bot.objects.get(id=request.POST['bot'])
        status = request.POST['status']
        player_play = request.POST['player_play']
        board = request.POST['Board'].split(',')
        Game.objects.create(
            player=player,
            bot=bot,
            status=status,
            player_play=player_play,
            board1=board[0],
            board2=board[1],
            board3=board[2],
            board4=board[3],
            board5=board[4],
            board6=board[5],
            board7=board[6],
            board8=board[7],
            board9=board[8],
        )

        player.total_games = player.total_games + 1
        bot.total_games = bot.total_games + 1
        if status == "WIN":
            player.total_win = player.total_win + 1
            bot.total_lose = bot.total_lose + 1
        elif status == "LOSE":
            player.total_lose = player.total_lose + 1
            bot.total_win = bot.total_win + 1
        elif status == "TIE":
            player.total_tie = player.total_tie + 1
            bot.total_tie = bot.total_tie + 1

        player.win_rate = (player.total_win/player.total_games)*100
        bot.win_rate = (bot.total_win/bot.total_games)*100
        player.save()
        bot.save()
    else:
        bot = Bot.objects.get(id=request.POST['bot'])
        status = request.POST['status']
        player_play = request.POST['player_play']
        board = request.POST['Board'].split(',')
        Game.objects.create(
            bot=bot,
            status=status,
            player_play=player_play,
            board1=board[0],
            board2=board[1],
            board3=board[2],
            board4=board[3],
            board5=board[4],
            board6=board[5],
            board7=board[6],
            board8=board[7],
            board9=board[8],
        )

        bot.total_games = bot.total_games + 1
        if status == "WIN":
            bot.total_lose = bot.total_lose + 1
        elif status == "LOSE":
            bot.total_win = bot.total_win + 1
        elif status == "TIE":
            bot.total_tie = bot.total_tie + 1

        bot.win_rate = (bot.total_win/bot.total_games)*100
        bot.save()

    return redirect('/')


def learn(request):
    context = {}
    if request.user.is_authenticated:
        player = request.user.player_set.get()
        context['player'] = player
    return render(request, 'learns/learn.html', context)


def learn_ttt(request):
    context = {}
    if request.user.is_authenticated:
        player = request.user.player_set.get()
        context['player'] = player
    return render(request, 'learns/learn_ttt.html', context)


def learn_profile(request):
    context = {}
    if request.user.is_authenticated:
        player = request.user.player_set.get()
        context['player'] = player
    return render(request, 'learns/learn_profile.html', context)


def leaderboardPage(request):
    players = Player.objects.all().order_by("-win_rate", "-total_win", "-total_tie", "total_lose")
    paginator = Paginator(players, 15)
    page = request.GET.get('page')
    try:
        players = paginator.page(page)
    except PageNotAnInteger:
        players = paginator.page(1)
    except EmptyPage:
        players = paginator.page(paginator.num_pages())

    context = {'players': players}
    if request.user.is_authenticated:
        player = request.user.player_set.get()
        context['player'] = player
    return render(request, 'leaderboard/leaderboard.html', context)
