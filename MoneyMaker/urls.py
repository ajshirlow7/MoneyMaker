from django.urls import path, include
from .views import home_page_view, register_view, logout_view

urlpatterns = [
    path("", home_page_view, name="home"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("play/", include("game.urls")),  
]