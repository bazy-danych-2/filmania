from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField
from movies.models import Movie

# Create your models here.

class User_info(models.Model):
   user =  OneToOneField(User, on_delete=CASCADE)
   ulubione_filmy = ManyToManyField(Movie, blank=True, null=True)

   def __str__(self):
       return f"{self.user.username} - {self.pk}"