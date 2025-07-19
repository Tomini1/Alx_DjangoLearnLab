from django.urls import path, include
from .views import list_books, LibraryDetailView
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView




urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]


from .views import login_view, logout_view, register_view, list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]

from .views import admin_view, librarian_view, member_view

urlpatterns += [
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]


from .views import add_book, edit_book, delete_book

urlpatterns = [
    

    path('book/add/', add_book, name='add_book'),
    path('book/<int:pk>/edit/', edit_book, name='edit_book'),
    path('book/<int:pk>/delete/', delete_book, name='delete_book'),
]



urlpatterns = [
    path('books/', list_books, name='list_books'),
]


urlpatterns += [
    path('register/', views.register, name='register'),  
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # ✅ LoginView with template
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # ✅ LogoutView with template
]

