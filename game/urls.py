from django.urls import path
from .views import play_view, leaderboard_view, review_page, delete_review, earn_money, delete_reply

urlpatterns = [
    path('', play_view, name='play'),
    path('leaderboard/', leaderboard_view, name='leaderboard'),
    path('review/', review_page, name='review'),
    path('review/delete/', delete_review, name='delete_review'),
    path('earn_money/', earn_money, name='earn_money'),
    path('reply/delete/<int:reply_id>/', delete_reply, name='delete_reply'),
]