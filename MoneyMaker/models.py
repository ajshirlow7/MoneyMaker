from django.db import models

# Create your models here.

class Review(models.Model):
    rating = models.IntegerField()
    text = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='moneymaker_reviews')
    # Add any other fields you need

    def __str__(self):
        return f"{self.user} - {self.rating} stars"
