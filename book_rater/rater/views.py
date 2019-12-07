from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book
from .models import Comment
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from rater.forms import CommentForm
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
          print(form.cleaned_data)
          comment = form.save(commit=False)
          comment.book = book
          comment.save()
          print(comment)
          return HttpResponseRedirect(reverse('rater:detail',args=(slug,)))

class CommentDetail(DetailView):
    model = Comment
    context_object_name = "comment"
    template_name = "comment_detail.html"