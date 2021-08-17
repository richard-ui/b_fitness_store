from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Reviews_list
from .forms import ReviewForm
from profiles.models import UserProfile
from django.db.models import Q
from django.db.models.functions import Lower
from django.http import JsonResponse
from django.template.loader import render_to_string

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
                # convert to lowercase
                reviews = reviews.annotate(lower_name=Lower('product'))
            if sortkey == 'product':  # take current category of product
                sortkey = 'product__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    # order products in descending order
                    sortkey = f'-{sortkey}'
                    # order by products from value of sortkey
            reviews = reviews.order_by(sortkey)

        if 'q' in request.GET: 
            query = request.GET['q']  # listens for input
            if not query:  # if query is empty provide error
                messages.error(
                    request,
                    "You didn't enter any search criteria!"
                    )
                return redirect(reverse('reviews_list'))

            # listen for search queries that are the same as
            # Product 'name' or 'description'
            queries = (
                Q(product__name__icontains=query)
            )
            reviews = reviews.filter(queries)  # filter out products

    current_sorting = f'{sort}_{direction}'

    context = {
        'reviews': reviews,
        'search_term': query,  # search box
        'current_sorting': current_sorting,
    }

    return render(request, 'reviews_list/reviews_list.html', context)


@login_required
def add_review(request):

    """ Add a Review for a product """

    if request.method == 'POST':  # validate form
        form = ReviewForm(request.POST)
        if form.is_valid():     
            instance = form.save(commit=False)  # form save/form
            # user session
            instance.user = UserProfile.objects.get(user=request.user)
            instance.save()  # save form instance
            messages.success(request, 'Your Review has been Added!')
            return redirect(reverse('reviews_list'))
        else:
            messages.error(
                request,
                'Failed to add Review. Please ensure the form is valid.'
                )
    else:
        form = ReviewForm()

    template = 'reviews_list/add_review.html'  # render add reviews page
    context = {
        'form': form,
    }

    return render(request, template, context)


#  edit function to update products for admin users only
@login_required
def edit_review(request, review_id):
    """ Edit a product in the store """

    review = get_object_or_404(Reviews_list, pk=review_id)  # get review id

    if request.method == 'POST':  # get ProductForm request
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():  # check for form validation
            form.save()
            messages.success(request, 'Successfully updated Review!')
            return redirect(reverse('products', args=[review.id]))
        else:
            messages.error(
                request,
                'Failed to update Review. Please ensure the form is valid.'
                )
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing review for {review.product}')

    template = 'reviews_list/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }
    return render(request, template, context)


#  delete function to delete products for admin users only
@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Reviews_list, pk=review_id)
    data = dict()
    if request.method == 'POST':
        review.delete()
        # This is just to play along with the existing code
        data['form_is_valid'] = True
        reviews = Reviews_list.objects.all()
        messages.success(request, 'Review deleted!')
        return redirect(reverse('products'))
    else:
        context = {'review': review}
        data['html_form'] = render_to_string(
            'reviews_list/includes/partial_review_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

