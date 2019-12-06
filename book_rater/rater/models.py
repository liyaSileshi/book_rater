from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 200, default='book title', null=True)
    description = models.TextField(default='book description')

class Comment(models.Model):
    comment = models.TextField(default='book comment')
    book = models.ForeignKey(Book, on_delete = models.CASCADE)