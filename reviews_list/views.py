from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Reviews_list
from .forms import ReviewForm
from profiles.models import UserProfile

# Create your views here.

def all_reviews(request):
   
    """ A view to show all products, including sorting and search queries """

    reviews = Reviews_list.objects.all()  # fetch reviews
    context = {
        'reviews': reviews,
        #'data' : [1, 2, 3, 4, 5],
    }

    return render(request, 'reviews_list/reviews_list.html', context)

@login_required
def add_review(request):

    """ Add a Review for a product """

    if request.method == 'POST': # validate form
        form = ReviewForm(request.POST)

        if form.is_valid():     
            instance = form.save(commit=False) # form save/form instance
            instance.user = UserProfile.objects.get(user=request.user)
            instance.save()
            messages.success(request, 'Your Review has been Added!')
            return redirect(reverse('reviews_list'))
        else:
            messages.error(
                request,
                'Failed to add Review. Please ensure the form is valid.'
                )
    else:
        form = ReviewForm()

    template = 'reviews_list/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)