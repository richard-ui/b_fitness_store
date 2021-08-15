from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import WishlistForm
from products.models import Product
from profiles.models import UserProfile
from .models import Wishlist


def view_wishlist(request):
    """ A view that renders the wishlist contents page """

    # basic view for displaying wishlist page

    Wishlist1 = Wishlist.objects.filter(pk=1)

    for product in Wishlist1.product.all():
        print(product.name, product.price)

    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, product_id):

    

    return render(request)
