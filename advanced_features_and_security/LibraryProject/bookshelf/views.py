from django.shortcuts import render

from .forms import BookSearchForm
from django.contrib.auth.decorators import permission_required

def secure_form_view(request):
    form = BookSearchForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # Process the form securely
        title = form.cleaned_data['title']
        # Use ORM to safely query
        from .models import Book
        books = Book.objects.filter(title__icontains=title)
        return render(request, 'bookshelf/book_list.html', {'books': books})
    return render(request, 'bookshelf/form_example.html', {'form': form})



@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Your view logic here
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    # Your view logic here
    pass
