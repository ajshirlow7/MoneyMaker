from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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


@receiver(post_save, sender=User)
def create_user_gamestate(sender, instance, created, **kwargs):
    if created:
        GameState.objects.create(user=instance)
