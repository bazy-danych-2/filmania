from typing import ContextManager
from django.shortcuts import render
from django.views import View
from movies.models import Movie

# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):

        movies = Movie.objects.filter(ratings__isnull=False).order_by('ratings__average')[:6]

       
        context = {

            'movies': movies
        }

        return render(request, 'pages/index.html', context)



class Final(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/final.html')