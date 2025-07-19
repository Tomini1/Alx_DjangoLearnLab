from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(name):
    author = Author.objects.get(name=name)
    return Book.objects.filter(author=author)

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)

author_name = 'Chinua Achebe'
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

for book in books_by_author:
    print(book.title)


library_name = 'Central Library'
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

for book in books_in_library:
    print(book.title)


library_name = 'Central Library'
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)

print(librarian.name)
