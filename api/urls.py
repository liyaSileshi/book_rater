from django.urls import path

from api.views import BookList, BookDetail, CommentList, CommentDetail

urlpatterns = [
    path('books/', BookList.as_view(), name='books_list'),
    path('books/<int:pk>', BookDetail.as_view(), name='books_detail'),
    path('comments/', CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>', CommentDetail.as_view(), name='comment_detail'),
]
