from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

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
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST: # checks for product size
        size = request.POST['product_size']

    # creates new dictionary in variable named bag
    bag = request.session.get('bag', {}) 

    if size:
        if item_id in list(bag.keys()): # if item already in bag
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request,
                    f'Updated size {size.upper()} {product.name}'
                    'quantity to {bag[item_id]["items_by_size"][size]}'
                    )
            else:
                # if product has size add a message alerting user 
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request,
                    f'Added size {size.upper()} {product.name} to your bag'
                    )
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request,
                f'Added size {size.upper()} {product.name} to your bag'
                )
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} to your {bag[item_id]}'
                )
        else:
            bag[item_id] = quantity # add product to bag with success message!
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag # gather current bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0: # if quantity greater than 0
            bag[item_id]['items_by_size'][size] = quantity # place quantity value in bag
            messages.success(
                request,
                f'Updated size {size.upper()} {product.name}'
                'quantity to {bag[item_id]["items_by_size"][size]}'
                )
        else:
            del bag[item_id]['items_by_size'][size] # else remove producy from bag
            if not bag[item_id]['items_by_size']: # if bag with size not set remove product
                bag.pop(item_id) 
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
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size: # if product has size delete the product from bag and
                   # delete items_by_size
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']: # if does not have items_by_size
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} {product.name} from your bag'
                )
        else:
            bag.pop(item_id) # else simply remove from your bag using pop function
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.danger(request, f'Error removing item {e}')
        return HttpResponse(status=500)
