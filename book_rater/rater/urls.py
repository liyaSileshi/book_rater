from django.urls import path
from rater.views import BookListView, BookDetailView
from . import views

app_name = 'rater'
urlpatterns = [
    path('', BookListView.as_view(), name='index'),
    path('<str:slug>/', BookDetailView.as_view(), name='detail'),
]
