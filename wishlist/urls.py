from django.urls import path
from . import views

urlpatterns = [
    path('<int:wishlist_id>/', views.view_wishlist, name='view_wishlist'),
    path('add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
]
