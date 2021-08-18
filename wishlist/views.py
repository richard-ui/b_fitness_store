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
    wishlist = Wishlist.objects.get_or_create(user=user)
    
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
    ) # get or create user

    #if wishlist.products.filter(product_wish).exists():
    # if wishlist id == product id passed
    if wishlist.products.filter(id=request.user.id).exists():
        #wishlist.products.remove(product_wish)
        messages.warning(request, "Item already added to wishlist")
    else:
        wishlist.products.add(product_wish)
        messages.success(request, "Item added to Wishlist!")
    #else:
	#wishlist.products.add(product_wish)
	#messages.success(request, "Item added to Wishlist!")
        

    return redirect(reverse('products'))
