from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Reviews_list
from .forms import ReviewForm
from products.models import Product
from profiles.models import UserProfile
from django.db.models import Q
from django.db.models.functions import Lower
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.


@login_required
def add_review(request, product_id):

    """ Add a Review for a product """

    product = get_object_or_404(Product, id=product_id) # get product    

    if request.method == 'POST':  # validate form
        form = ReviewForm(request.POST)
        if form.is_valid():     
            instance = form.save(commit=False)  # form save/form
            # user session
            instance.user = UserProfile.objects.get(user=request.user)
            instance.product = product
            instance.save()  # save form instance
            
            messages.success(request, 'Your Review has been Added!')
            return redirect(reverse('product_detail', args=[product.id]))
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
        'product': product,
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
            return redirect(reverse('product_detail', args=[review.product.id]))
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

