from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from core.models import Book

# Create your views here.
class indexView(TemplateView):
    template_name = 'core/index.html'

class bookDetail(DetailView):
    model = Book
    template_name = 'core/book_details.html'