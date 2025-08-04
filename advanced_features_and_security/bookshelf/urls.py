from django.urls import path
from .views import secure_form_view

urlpatterns = [
    path('secure-form/', secure_form_view, name='secure_form'),
]
