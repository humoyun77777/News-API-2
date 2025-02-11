from django.urls import path
from .views import CategoryAPI, NewsAPI
urlpatterns = [
    path('category/',CategoryAPI.as_view(),name = 'category'),
    path('category/<int:pk>/',CategoryAPI.as_view(),name = 'category'),
    path('news/',NewsAPI.as_view(),name = 'news'),
    path('news/<int:pk>/',NewsAPI.as_view(),name = 'news'),
]