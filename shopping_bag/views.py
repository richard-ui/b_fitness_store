from django.shortcuts import render


def view_bag(request):
    """ A view to that renders contents of bag """

    return render(request, 'bag/shopping_bag.html')
