from django.shortcuts import render

from .forms import BookSearchForm


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
