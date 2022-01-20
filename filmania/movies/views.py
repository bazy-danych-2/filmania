from audioop import reverse
from django.forms.fields import NullBooleanField
from django.shortcuts import redirect, render

from accounts.models import User_info
from django.http import HttpResponseRedirect

from .models import Movie
from django.contrib.auth.models import User
from .forms import MovieForm, UpdateMovieForm
from comments.models import Comment, Like
from comments.forms import CommentForm

# Create your views here.

def create_movie(request):

    form = MovieForm(request.POST, request.FILES)
    user = request.user
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author= user
            instance.save()
            return redirect("/movies/")
        else:
            print(form.errors)


    context = {

        'form': form,
    }

    return render(request,"movies/create.html",context)

def update_movie(request,id):

    user = request.user
    movie = Movie.objects.get(pk=id)
    
    form = UpdateMovieForm( request.POST or None, request.FILES or None ,instance=movie)
    if movie.author == user or user.is_superuser == True:
        

        if request.method == 'POST':
               if form.is_valid():
                     form.save()
                     return redirect("/movies/")
    else:
        return redirect(show_all_movies)
        
        

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
    is_fav = False
    user = request.user
    if request.user.is_authenticated:
         user_inf = User_info.objects.get(user = user)
        

         if movie not in user_inf.ulubione_filmy.all():
                 is_fav = True

    

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
        'is_fav': is_fav,
    }


    return render(request,"movies/details.html",context)

def delete_comment(request, id):

    author = request.user
    comment = Comment.objects.get(pk=id)
    
    if comment.user == author or author.is_superuser == True:
        

        if request.method == 'POST':
            print(request.POST)
            comment.delete()
            return redirect(show_all_movies)
              
    else:

        return redirect(show_all_movies)
        

    context={

    }

    return render(request,"movies/delete_com.html",context)


def delete_movie(request, id):

    user = request.user
    movie = Movie.objects.get(pk=id)

    if movie.author == user or user.is_superuser == True:
        

        if request.method == 'POST':
            print("dupa")
              
    else:

        return redirect(show_all_movies)
        

    context={

    }

    return render(request,"movies/delete.html",context)