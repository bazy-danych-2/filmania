from django.urls import path,include
from . import views

urlpatterns = [
    path('create/',views.create_movie, name='create-movie'),
    path('update/<int:id>/',views.update_movie, name='update-movie'),
    path('delete/<int:id>/',views.delete_movie, name='delete-movie'),
    path('delete_com/<int:id>/', views.delete_comment, name='delete-comment'),
    path('',views.show_all_movies, name='show_all'),
    path('details/<int:id>/',views.movie_details, name='details-movie'),
    

   
]
