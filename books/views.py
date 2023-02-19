from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.db.models import F, Max, Min, Avg, Count
from .models import Book
# Create your views here.
class BooksTemplateView(TemplateView):
    template_name = 'books.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Book.objects.all().update(number_pages = F('number_pages') + 1)
        
        context['books'] = Book.objects.annotate(number_sheets = (F('number_pages') / 2) )


        return context