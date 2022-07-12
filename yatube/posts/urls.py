# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Группы постов
    path('group/<slug:slug>/', views.group_posts),
]
