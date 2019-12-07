from django import forms
from rater.models import Comment
from rater.models import Book
from django.forms import ModelForm, TextInput

# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = [
#                 'title'
#             ]
#         widgets = {
#             'title': TextInput(attrs={'class' : 'input', 'name':'q', 'placeholder' : 'Book Name'}),
#         }

class CommentForm(forms.ModelForm):
    """ Render and process a form based on the Comment model. """
    class Meta:
        model = Comment
        fields = [
                'comment',
                'rating'
            ]
