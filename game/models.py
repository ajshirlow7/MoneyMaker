from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ({self.rating} stars)"


class GameState(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s GameState"
