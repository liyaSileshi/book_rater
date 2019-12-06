from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 200, default='book title', null=True)
    description = models.TextField(default='book description')

class Comment(models.Model):
    RATING_RANGE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    comment = models.TextField(default='book comment')
    rating = models.IntegerField(choices=RATING_RANGE, default=RATING_RANGE[0][0])
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    def __str__(self):
        return self.comment
        