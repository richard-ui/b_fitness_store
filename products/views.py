import json
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import JsonResponse
from .models import Product, Category
from .forms import ProductForm

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()  # fetch all products
    query = None
    categories = None
    sort = None
    direction = None # set all variables to none at first
    paginator = None

    page = request.GET.get('page', 1)

    paginator = Paginator(products, 20) # paginator function to paginate by 20 products

    # listens for get request, either sorting or by category
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name': # take current name of product
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name')) # convert to lowercase
            if sortkey == 'category': # take current category of product
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'  # order products in descending order
            products = products.order_by(sortkey) # order by products from value of sortkey

        if 'category' in request.GET: # gets category request
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # search request function
        if 'q' in request.GET: 
            query = request.GET['q'] # listens for input
            if not query:  # if query is empty provide error
                messages.error(
                    request,
                    "You didn't enter any search criteria!"
                    )
                return redirect(reverse('products'))

            # listen for search queries that are the same as Product 'name' or 'description'
            queries = (
                Q(name__icontains=query) | Q(description__icontains=query) 
            )
            products = products.filter(queries) # filter out products

    current_sorting = f'{sort}_{direction}'

    # pagination
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'search_term': query, # search box
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    
    """ Add a product to the store """
    if not request.user.is_superuser: # if NOT superuser
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home')) # redirect back to home page

    if request.method == 'POST': # validate form
        form = ProductForm(request.POST, request.FILES) 
        if form.is_valid():
            product = form.save() # form save
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
                )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


#  edit function to update products for admin users only
@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser: # check to see if NOT superuser
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home')) # redirect to home page

    product = get_object_or_404(Product, pk=product_id) # get product id
    if request.method == 'POST': # get ProductForm request
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid(): # check for form validation
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.'
                )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


#  delete function to delete products for admin users only
@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    data = dict()
    if request.method == 'POST':
        product.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        products = Product.objects.all()
        messages.success(request, 'Product deleted!')
        return redirect(reverse('products'))
    else:
        context = {'product': product}
        data['html_form'] = render_to_string('products/includes/partial_book_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)


def auto(request):  # autocomplete function for search box
    if 'term' in request.GET:
        qs = Product.objects.filter(name__icontains=request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.append(product.name)

        return JsonResponse(titles, safe=False)
    return render(request, 'products/products.html')
