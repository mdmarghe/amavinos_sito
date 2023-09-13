from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<slug:slug>/', views.article_details, name='article_detail'),
    path('article_create/', views.article_create, name="article_create"),

]
