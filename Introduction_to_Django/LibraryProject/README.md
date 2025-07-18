**`📚 LibraryProject`**

This is a beginner Django project built as part of the ALX Back-End curriculum.

**`Contents`**

Django Project: LibraryProject

App: bookshelf

Model: Book with fields:

title (CharField, max_length=200)

author (CharField, max_length=100)

publication_year (IntegerField)

**`Features`**

Full CRUD operations using Django ORM

Admin interface integration with:

List display of book fields

Search by title and author

Filter by publication year

Markdown documentation for each operation:

create.md, retrieve.md, update.md, delete.md

CRUD_operations.md (summary)

**`How to Run`**

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

Visit the admin panel at: http://127.0.0.1:8000/admin
