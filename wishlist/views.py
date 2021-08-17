from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import WishlistForm
from products.models import Product
from profiles.models import UserProfile
from .models import Wishlist


def view_wishlist(request, wishlist_id):
    """ A view that renders the wishlist contents page """

    # basic view for displaying wishlist page
    #wishlist = Wishlist.objects.get(id=wishlist_id)

    wishlist = get_object_or_404(Wishlist, pk=wishlist_id)
    
    context={
        'wishlist': wishlist,
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):

    product = get_object_or_404(Product, pk=product_id) # get product
    wish_list = Wishlist.objects.get_or_create(user=request.user, product=product)
    # wish_list1 = Wishlist.objects.get(pk=1)
    # wish_list1.product = product
    wish_list.save()
    #wish_list.add_to_wishlist(product_id)

    messages.success(request, "Wishlist updated!")

    return redirect(reverse('products'))
