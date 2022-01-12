from typing import Callable
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from movies.models import Movie


# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    movie = models.ForeignKey(Movie, on_delete=CASCADE, related_name='comments')
    liked = models.ManyToManyField(User, default=None, related_name='likes', blank=True)
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def num_likes(self):
        return self.liked.all().count()
    
    class Meta:
        ordering = ('-created',)
    
Like_Choice = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    comment = models.ForeignKey(Comment, on_delete=CASCADE)
    value = models.CharField(choices=Like_Choice, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)