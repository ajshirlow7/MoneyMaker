from django.urls import path
from .views import play_view

urlpatterns = [
    path('', play_view, name='play'),
]