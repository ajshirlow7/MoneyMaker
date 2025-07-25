from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def play_view(request):
    return render(request, "game/play.html")

@login_required
def leaderboard_view(request):
    users = User.objects.all().order_by('username')  # You can order by any field you want
    return render(request, "game/leaderboard.html", {"users": users})
