from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from django.http import JsonResponse
from django.template.loader import render_to_string

from products.models import Product
# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    # basic view for displaying shop bag page

    return render(request, 'bag/shopping_bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id) # get product id
    quantity = int(request.POST.get('quantity')) # get quantity of selected products
    redirect_url = request.POST.get('redirect_url') # redirects to the same page
    size = None
    if 'product_size' in request.POST: # checks for product size
        size = request.POST['product_size']

    # check to see if bag session exists, if not create one.
    bag = request.session.get('bag', {}) 

    # if size or shoe_size being added
    if size:
        # if item key already in bag
        if item_id in list(bag.keys()):
            #  check if another item of the same id and same size already exists.
            if size in bag[item_id]['items_by_size'].keys():
                # if so increment quantity of that size
                bag[item_id]['items_by_size'][size] += quantity
                messages.success( # toast success shows
                    request,
                    f'Updated size {size.upper()} {product.name}'
                    'quantity to {bag[item_id]["items_by_size"][size]}'
                    )
            else:
                # else just set it to the quantity
                bag[item_id]['items_by_size'][size] = quantity
                messages.success( # toast success shows
                    request,
                    f'Added size {size.upper()} {product.name} to your bag'
                    )
        else:
            # if items not already in the bag, we can just add it
            # with a key of 'items_by_size'
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success( # toast success message
                request,
                f'Added size {size.upper()} {product.name} to your bag'
                )
    else:
        # if no size we run this logic
        # if item_id in keys list
        if item_id in list(bag.keys()):
            bag[item_id] += quantity # just increment quantity of product
            messages.success( # toast success shows
                request, f'Updated {product.name} to your {bag[item_id]}'
                )
        else:
            # else just add item to bag
            bag[item_id] = quantity 
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag # gather current bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    # product id
    product = get_object_or_404(Product, pk=item_id)

    # input quantity box
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # check for bag session otherwsie create new dictionary
    bag = request.session.get('bag', {}) 

    if size:
        if quantity > 0: # if input quantity greater than 0
            bag[item_id]['items_by_size'][size] = quantity # place quantity input value in bag
            messages.success(
                request,
                f'Updated size {size.upper()} {product.name}'
                'quantity to {bag[item_id]["items_by_size"][size]}'
                )
        else:
            del bag[item_id]['items_by_size'][size] # else delete product from bag
            if not bag[item_id]['items_by_size']: # if bag with size not set.
                bag.pop(item_id) # remove product using pop function
            messages.success(
                request,
                f'Removed size {size.upper()} {product.name} from your bag'
                )
    else:
        if quantity > 0: # if quantity greater than 0
            bag[item_id] = quantity # set quantity to product id from bag
            messages.success(
                request,
                f'Updated {product.name} quantity to your {bag[item_id]}')
        else:
            bag.pop(item_id) # else just remove from your bag
            messages.danger(request, f'Removed {product.name} to your bag')

    request.session['bag'] = bag # set a session for the bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    
    try:
        product = get_object_or_404(Product, pk=item_id)
        data = dict()
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size: # if product has size delete the product from bag and
                   # delete items_by_size
            del bag[item_id]['items_by_size'][size]

            if not bag[item_id]['items_by_size']: # if does not have items_by_size
                bag.pop(item_id) # delete item_id from bag
            messages.success(
                request,
                f'Removed size {size.upper()} {product.name} from your bag'
                )
        else:
            bag.pop(item_id) # else simply remove from your bag using pop function
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag # request current session 'bag'
        return HttpResponse(status=200)

    except Exception as e:
        messages.danger(request, f'Error removing item {e}')
        return HttpResponse(status=500)
