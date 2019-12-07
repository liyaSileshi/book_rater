from django import forms
from rater.models import Comment


class CommentForm(forms.ModelForm):
    """ Render and process a form based on the Comment model. """
    class Meta:
        model = Comment
        fields = [
                'comment'
            ]