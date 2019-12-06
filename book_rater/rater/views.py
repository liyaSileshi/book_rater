from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book
from .models import Comment
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
# Create your views here.

class BookListView(ListView):
    """ Renders a list of all Books. """
    model = Book
    def get(self, request):
        """ GET a list of Books. """
        books = self.get_queryset().all()
        return render(request, 'rater/index.html', {
          'books': books
        })

class BookDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Book

    def get(self, request, slug):
        """ Returns a specific book by slug. """
        book = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'rater/detail.html', {
          'book': book
        })   

# def index(request):
#     all_books = Book.objects.all()
#     context = {'all_books': all_books}
#     return render(request, 'rater/index.html', context)


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'rater/detail.html', {'book': book})