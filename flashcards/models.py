from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass

class Deck(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/', blank=True, null=True,)
    
    def publish(self):
        self.publish_date = timezone.now()
        self.save

    def __str__(self):
        return self.title
    

class Card(models.Model):
    front = models.CharField(max_length=50)
    back = models.TextField()
    deck = models.ForeignKey('Deck', on_delete=models.CASCADE,null=True, blank=True, related_name='cards')

    def publish(self):
        self.save

    def __str__(self):
        return self.front