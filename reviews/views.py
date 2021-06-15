from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm

# Create your views here.

def all_reviews(request):
   
    """ A view to show all products, including sorting and search queries """

    reviews = Review.objects.all()  # fetch reviews
    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/reviews.html', context)

@login_required
def add_review(request):

    """ Add a Review for a product """

    if request.method == 'POST': # validate form
        form = ReviewForm(request.POST)
        form = Review(
            review=request.POST.get('review'),
            user=request.user
        )
        if form.is_valid():     
            review = form.save() # form save
            messages.success(request, 'Your Review has been Added!')
            return redirect(reverse('reviews'))
        else:
            messages.error(
                request,
                'Failed to add Review. Please ensure the form is valid.'
                )
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)