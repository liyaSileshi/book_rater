from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book
from .models import Comment
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from rater.forms import CommentForm
import requests
import json
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

    # def get(self, request):
    #     name = request.GET.get('q', '')
    #     url = 'https://www.googleapis.com/books/v1/volumes?q={}'
    #     # response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={}')
    #     book_db = Book.objects.all()
    #     name = 'Bad Blood'
    #     book_array = {}
    #     form = BookForm()
    #     books = requests.get(url.format(name)).json() #request the API data and convert the JSON to Python data types
    #     print(books)
    #     # json.data = json.loads(books['items'])
    #     # print(json.data)
    #     results = books['items']

    #     # for book in book_db:
        
    #     # print(results)
    #     for book in results:
    #         # book_array.append(book['volumeInfo']['imageLinks']['thumbnail'])
    #         book_array[book['id']] = book['volumeInfo']['imageLinks']['thumbnail']
    #         # book['id']
    #     print(book_array)
    #     context = {'book_array':book_array, 'form':form}
    #     # print(context)
        
    #     return render(request, 'rater/index.html', context) #returns the index.html template

    # def post(self, request):
    #     pass

class BookDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Book

    def get(self, request, slug):
        """ Returns a specific book by slug. """
        book = self.get_queryset().get(slug__iexact=slug)
        form = CommentForm()
        context = {
        'book': book,
        'form' : form
        }
        return render(request, 'rater/detail.html', context)   

    def post(self, request, slug):
        book = self.get_queryset().get(slug__iexact=slug)
        form = CommentForm(request.POST)
        if form.is_valid():
        #   print(form.cleaned_data)
          comment = form.save(commit=False)
          comment.book = book
          comment.save()
        #   print(comment)
          return HttpResponseRedirect(reverse('rater:detail',args=(slug,)))

class CommentDetail(DetailView):
    model = Comment
    context_object_name = "comment"
    template_name = "comment_detail.html"