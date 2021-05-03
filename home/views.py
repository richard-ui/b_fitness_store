import json

from django.http import JsonResponse
from django.shortcuts import render

from home.models import Product_item


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def autocomplete(request):
    if 'term' in request.GET:
        qs = Product_item.objects.filter(title__icontains=request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.append(product.title)
        # titles = [product.title for product in qs]
        return JsonResponse(titles, safe=False)
    return render(request, 'home/home.html')
