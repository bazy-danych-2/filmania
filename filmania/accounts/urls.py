from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.register),
    path('hello/',views.user_panel),

    path('login/',views.viev_login),
]
