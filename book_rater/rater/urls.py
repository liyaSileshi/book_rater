from django.urls import path
from rater.views import BookListView
from . import views

app_name = 'rater'
urlpatterns = [
    path('', BookListView.as_view(), name='index'),
    path('<int:book_id>/', views.detail, name='detail'),
]