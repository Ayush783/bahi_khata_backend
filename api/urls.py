from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('register/<str:id>/', views.register),
    path('user/<str:id>/data/', views.userdata),
]
