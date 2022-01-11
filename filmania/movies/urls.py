from django.urls import path,include
from . import views

urlpatterns = [
    path('create/',views.create_movie, name='create-movie'),
    path('update/<int:id>/',views.update_movie, name='update-movie'),
    path('',views.show_all_movies, name='show_all'),
    path('details/<int:id>/',views.movie_details, name='details-movie'),
    

   
]
