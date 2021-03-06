from django.shortcuts import render, redirect
from datetime import date
from .models import Game, Player, Table, Champ
# Create your views here.

def home(request):
    games=Game.objects.all().order_by('game_year', 'game_month', 'game_day', 'game_no')
    champ=Champ.objects.all().order_by('game_year', 'game_month', 'game_day', 'game_no')
    return render(request, 'home.html',{'games':games, 'champ':champ})

def table(request):
    tables=Table.objects.order_by('-team_point','-team_goal')
    return render(request, 'table.html',{'tables':tables})

def stats(request):
    stats=Player.objects.order_by('-player_goals')
    return render(request, 'stats.html',{'stats':stats})

def players(request):
    players=Player.objects.all().order_by('player_name')
    return render(request, 'players.html',{'players':players})

