from django import template


register = template.Library()

# function for multiplying price by the quantity of the product
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
