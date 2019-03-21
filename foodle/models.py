from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class DealModel(models.Model):
    info = models.CharField(default='', max_length=200)
    picture = models.ImageField(upload_to='deals/', blank=True)
    likes = models.IntegerField(default=0)
    category = models.CharField(default='', max_length=50)

    @property
    def add_like(self):
       self.likes += 1

class BlogPost(models.Model):
    """
    The "BlogPost" model for the foodle  app
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    body = models.CharField(default='', max_length=200)

    def __str__(self):
        return self.body
