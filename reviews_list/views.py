from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Reviews_list
from .forms import ReviewForm
from profiles.models import UserProfile
from django.db.models import Q
from django.db.models.functions import Lower
from django.http import JsonResponse

# Create your views here.

def all_reviews(request):
   
    """ A view to show all products, including sorting and search queries """

    # set all variables to none at first

    reviews = Reviews_list.objects.all()  # fetch reviews
    query = None
    sort = None
    direction = None

    # search request function
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'product':
                sortkey = 'lower_name'
                reviews = reviews.annotate(lower_name=Lower('product')) # convert to lowercase
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'  # order products in descending order
            reviews = reviews.order_by(sortkey) # order by products from value of sortkey

        if 'q' in request.GET: 
            query = request.GET['q'] # listens for input
            if not query:  # if query is empty provide error
                messages.error(
                    request,
                    "You didn't enter any search criteria!"
                    )
                return redirect(reverse('reviews_list'))

            # listen for search queries that are the same as Product 'name' or 'description'
            queries = (
                Q(product__name__icontains=query)
            )
            reviews = reviews.filter(queries) # filter out products

    current_sorting = f'{sort}_{direction}'

    context = {
        'reviews': reviews,
        'search_term': query, # search box
        'current_sorting': current_sorting,
    }

    return render(request, 'reviews_list/reviews_list.html', context)

@login_required
def add_review(request):

    """ Add a Review for a product """

    if request.method == 'POST': # validate form
        form = ReviewForm(request.POST)

        if form.is_valid():     
            instance = form.save(commit=False) # form save/form
            instance.user = UserProfile.objects.get(user=request.user) # user session
            instance.save() # save form instance
            messages.success(request, 'Your Review has been Added!')
            return redirect(reverse('reviews_list'))
        else:
            messages.error(
                request,
                'Failed to add Review. Please ensure the form is valid.'
                )
    else:
        form = ReviewForm()

    template = 'reviews_list/add_review.html' # render add reviews page
    context = {
        'form': form,
    }

    return render(request, template, context)


def auto_review(request):  # autocomplete function for search box
    if 'term' in request.GET:
        qs = Reviews_list.objects.filter(product__name__icontains=request.GET.get('term'))
        titles = list()
        for review in qs:
            titles.append(review.product.name)

        return JsonResponse(titles, safe=False)
    return render(request, 'reviews_list/reviews_list.html')