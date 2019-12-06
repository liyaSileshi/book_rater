from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book
# Create your views here.
def index(request):
    all_books = Book.objects.all()
    context = {'all_books': all_books}
    return render(request, 'rater/index.html', context)


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'rater/detail.html', {'book': book})
    