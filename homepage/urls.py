from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers
from . import views
urlpatterns = [
    path('restview/',views.getnotes),
    path('restview/<str:pk>/update/',views.updatefullnote),
    path('restview/<str:pk>/delete/',views.deletefullnote),
    path('restview/create/',views.createfullnote),
    path('restview/<str:pk>/',views.getfullnote),
    ]
