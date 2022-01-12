from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import  CreateUserForm
from movies.models import Movie
from star_ratings.models import UserRating

def register(request):
    form = CreateUserForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        form.save()

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

def user_panel(request):
    return render(request,"hello.html",{} )



