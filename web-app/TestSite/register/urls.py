from django.urls import path
from . import views
urlpatterns = [
    path('', views.register_home.as_view(), name='register'),
    path('login/', views.LogInUser.as_view(), name='login'),
    path('logout/', views.logOutUser, name='logout'),
    path('register_page2', views.register_page2, name='register_page_2'),
    path('redact_profile', views.redact, name='redact_profile'),
]
