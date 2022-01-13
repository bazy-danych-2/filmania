from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import  CreateUserForm
from movies.models import Movie
from star_ratings.models import UserRating
from .models import User_info
from movies.views import movie_details

def register(request):
    form = CreateUserForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data.get("email")

        user = form.save()

        user_inf = User_info(user = user)
        user_inf.save()

        login(request, user)



    context={
        'form':form
    }

    return render(request,"register.html",context)



def viev_login(request):

    
    context={
     
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect(user_panel)
        else:
            messages.info(request,'Username or password is incorrect')
            return  render(request,"login.html",context)
  



    return  render(request,"login.html",context)

def add_to_fav(request):

    user = request.user
    
    id = request.POST['id']
    movie = Movie.objects.get(pk = id)

    user_inf = User_info.objects.get(user = user)

    if movie not in user_inf.ulubione_filmy.all():
        user_inf.ulubione_filmy.add(movie)
        user_inf.save()
    else:
        user_inf.ulubione_filmy.remove(movie)
        user_inf.save()




    return redirect(movie_details, id =id )

    

def user_panel(request):
    user = request.user
    user_inf = User_info.objects.get(user = user)

    movies = user_inf.ulubione_filmy.all()
    


    context = {
        'movies': movies
    }

    return render(request,"hello.html", context )



