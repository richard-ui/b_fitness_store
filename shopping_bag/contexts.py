from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []  # create array object
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})  # created bag session

    # for loop to loop through shop bag items
    for item_id, item_product in bag.items():
        # execute code if item has no sizes
        if isinstance(item_product, int):
            # get current product id
            product = get_object_or_404(Product, pk=item_id)
            total += item_product * product.price
            product_count += item_product  # product count
            bag_items.append({
                'item_id': item_id,   # append id, quantity and product 
                'quantity': item_product,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_product['itemsSize'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    # if bag total less than '50'
    if total < settings.FREE_DELIVERY_THRESHOLD:
        # delivery = bag total x 10%
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        # free delivery delta =
        # how much user would need to spend for free delivery
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        # else reset delivery charge to 0.
        delivery = 0
        free_delivery_delta = 0
    # grand total taking into consideration the delivery cost.
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context  # context available in any template file thoughout app
