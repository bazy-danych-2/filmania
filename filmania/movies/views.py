from django.forms.fields import NullBooleanField
from django.shortcuts import redirect, render

from .models import Movie
from django.contrib.auth.models import User
from .forms import MovieForm, UpdateMovieForm
from comments.models import Comment, Like
from comments.forms import CommentForm

# Create your views here.

def create_movie(request):

    form = MovieForm(request.POST)
    user = request.user
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author= user
            instance.save()


    context = {

        'form': form,
    }

    return render(request,"movies/create.html",context)

def update_movie(request,id):

    user = request.user
    movie = Movie.objects.get(pk=id)
    

    if movie.author == user or user.is_superuser == True:
        form = UpdateMovieForm( request.POST or None, request.FILES or None ,instance=movie)

        if request.method == 'POST':
               if form.is_valid():
                     form.save()
    
        
        

    context={
        'form': form

    }

    return render(request,"movies/update.html",context)

def show_all_movies(request):

    movies = Movie.objects.all()
    context={
        'movies': movies

    }

    return render(request,"movies/all.html",context)

def movie_details(request, id):

    comments = Comment.objects.all()
    c_form = CommentForm(request.POST or None)
    movie = Movie.objects.get(pk=id)
    
    if c_form.is_valid():
        instance = c_form.save(commit=False)
        instance.user = request.user
        instance.movie = Movie.objects.get(id=request.POST.get('movie_id'))
        instance.save()
        c_form = CommentForm()
        
        
    context={
        'movie': movie,
        'c_form': c_form,
        'comments': comments,
    }


    return render(request,"movies/details.html",context)