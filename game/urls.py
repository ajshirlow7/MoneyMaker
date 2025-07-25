from django.urls import path
from .views import play_view, leaderboard_view

urlpatterns = [
    path('', play_view, name='play'),
    path('leaderboard/', leaderboard_view, name='leaderboard'),
]