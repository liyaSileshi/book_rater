from django.contrib import admin

# Register your models here.
from .models import Book
from .models import Comment

admin.site.register(Book)
admin.site.register(Comment)