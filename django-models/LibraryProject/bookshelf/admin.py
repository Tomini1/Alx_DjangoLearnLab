
# Register your models here.
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these fields in list view
    search_fields = ('title', 'author')  # Enable search by title and author
    list_filter = ('publication_year',)  # Add filter by publication year

admin.site.register(Book, BookAdmin)
