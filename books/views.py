from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.template.loader import render_to_string

from .models import Book
from .forms import BookForm


# def book_list(request):
#     books = Book.objects.all()
#     context = {
#         'books': books,
#     }

#     return render(request, 'books/book_list.html', context)


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def book_create(request):
    data = dict()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = BookForm()

    context = {'form': form}
    data['html_form'] = render_to_string('books/includes/partial_book_create.html',
        context,
        request=request
    )
    return JsonResponse(data)


def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    data = dict()
    if request.method == 'POST':
        book.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        books = Book.objects.all()
        messages.success(request, 'Product deleted!')
        return redirect(reverse('products'))
    else:
        context = {'book': book}
        data['html_form'] = render_to_string('books/includes/partial_book_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)