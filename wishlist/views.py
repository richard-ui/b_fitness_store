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

@login_required
def view_wishlist(request):
    """ A view that renders the wishlist contents page """

    # basic view for displaying User wishlist page
    
    user = UserProfile.objects.get(user=request.user)

    wishlist = get_object_or_404(Wishlist, user=user)
    
    context={
        'wishlist': wishlist,
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):

    product_wish = get_object_or_404(Product, pk=product_id) # get product
    
    wishlist, created = Wishlist.objects.get_or_create(
        user=request.user.userprofile,
        name='rick'
    )


    if wishlist.products.filter(name=product_wish).exists():
        messages.warning(request, "Item already added to wishlist")
    else:
        wishlist.products.add(product_wish)
        messages.success(request, "Item added to Wishlist!")

    return redirect(reverse('products'))


@login_required
def remove_from_wishlist(request, product_id):

    product_wish = get_object_or_404(Product, pk=product_id) # get product
    user = UserProfile.objects.get(user=request.user) # get user

    wishlist = get_object_or_404(Wishlist, user=user) # filter wishlist item from with user

    wishlist.products.remove(product_wish) # remove item
    messages.success(request, 'Product Removed From Wishlist')

    return redirect(reverse('products'))

