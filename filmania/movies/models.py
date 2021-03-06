from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating


# Create your models here.


class Movie(models.Model):
    content = models.TextField()
    short_desc = models.CharField(max_length=255, null=False, blank=False, default="")
    model_img = models.ImageField(upload_to='movies_photos', blank=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    #takie dodatkowe informacje do filmu
    title = models.CharField(blank=False, null=False, max_length=50, default='')
    director = models.CharField(blank=True, null=True, max_length=50)
    scenariusz = models.CharField(blank=True, null=True, max_length=50)
    gatunek = models.CharField(blank=True, null=True, max_length=50)
    kraj = models.CharField(blank=True, null=True, max_length=50)
    data_premiery = models.DateField(null=True, blank=True)
    
    ratings = GenericRelation(Rating, related_query_name='rating')

    
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"{self.title} - {self.id}"


        