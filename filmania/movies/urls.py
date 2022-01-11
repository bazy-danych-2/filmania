from django.urls import path,include
from . import views

urlpatterns = [
    path('create/',views.create_movie, name='create-movie'),
    path('update/<int:id>/',views.update_movie, name='update-movie'),
    

   
]
