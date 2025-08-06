from django.urls import path, include
from .views import home_page_view, register_view, logout_view
from . import views

urlpatterns = [
    path("", home_page_view, name="home"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("play/", include("game.urls")),
    path("review/", views.review_view, name="review"),
    path("review/delete/", views.delete_review, name="delete_review"),
    path("review/reply/delete/<int:reply_id>/", views.delete_reply, name="delete_reply"),
]