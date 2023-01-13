from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {
            'user_name':'Numele tau',
            'user_email':'Adresa ta de e-mail',
            'text': 'Comentariul tau'
        }