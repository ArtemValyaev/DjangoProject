from django.urls import path

from . import views


urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
    path('like/', views.like_news, name='like-news'),
    path('liked/', views.news_liked, name='news_liked'),
    path('search', views.search, name='search'),
    path('<str:category>', views.cat, name='category'),

]
