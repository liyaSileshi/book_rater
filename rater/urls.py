from django.urls import path
from rater.views import BookListView, BookDetailView, BookCreateView
from . import views

app_name = 'rater'
urlpatterns = [
    path('', BookListView.as_view(), name='index'),
    path('new/', BookCreateView.as_view(), name='newBook'),
    path('<str:slug>/', BookDetailView.as_view(), name='detail'),
]
