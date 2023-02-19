from django.urls import path
from .views import BooksTemplateView
urlpatterns = [
    path('', BooksTemplateView.as_view(), name='books_view'),
]