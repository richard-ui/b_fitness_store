from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_reviews, name='reviews_list'),
    path('add/', views.add_review, name='add_review'),
    path('auto_review/', views.auto_review, name='auto_review'),
]
