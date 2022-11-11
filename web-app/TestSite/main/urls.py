from django.urls import path
from . import views

urlpatterns = [
    path('', views.recomendations, name='home'),
    path('profile', views.profile, name='profile'),
]
