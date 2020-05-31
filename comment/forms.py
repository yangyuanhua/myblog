from django import forms
from .models import Comment


class CommentForms(forms.ModelForm):

    class Meta:

        model = Comment
        fields = ["name","email","url","text"]