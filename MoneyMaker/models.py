from django.db import models

# Create your models here.

class Review(models.Model):
    rating = models.IntegerField(null=True, blank=True)
    text = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='moneymaker_reviews')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.rating} stars"
