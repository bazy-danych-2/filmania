from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.register),
    path('hello/',views.user_panel),

    path('login/',views.viev_login),
    path('add_fav/',views.add_to_fav),
    path('log_out', views.log_out),
]
