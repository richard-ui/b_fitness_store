import json

from django.http import JsonResponse
from django.shortcuts import render

from home.models import Product


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def autocomplete(request):
    if 'term' in request.GET:
        qs = Product.objects.filter(Name__icontains=request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.append(product.title)
        return JsonResponse(titles, safe=False)
    return render(request, 'home/index.html')
