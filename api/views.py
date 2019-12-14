from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rater.models import Book, Comment
from api.serializers import BookSerializer
from api.serializers import CommentSerializer

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()[:20]
        data = BookSerializer(books, many=True).data
        return Response(data)

class BookDetail(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        data = BookSerializer(book).data
        return Response(data)

class CommentList(APIView):
    def get(self, request):
        comments = Comment.objects.all()[:20]
        data = CommentSerializer(comments, many=True).data
        return Response(data)

class CommentDetail(APIView):
    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        data = CommentSerializer(comment).data
        return Response(data)