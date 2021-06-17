from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Reviews_list
from .forms import ReviewForm
from profiles.models import UserProfile
from django.db.models import Q

# Create your views here.

def all_reviews(request):
   
    """ A view to show all products, including sorting and search queries """

    reviews = Reviews_list.objects.all()  # fetch reviews
    query = None

    # search request function
    if request.GET:
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

    context = {
        'reviews': reviews,
        'search_term': query, # search box
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