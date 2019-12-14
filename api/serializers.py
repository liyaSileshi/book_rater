from rest_framework.serializers import ModelSerializer

from rater.models import Book, Comment

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'