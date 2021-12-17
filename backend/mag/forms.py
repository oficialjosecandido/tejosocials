from django import forms

from .models import *


class newPost(forms.ModelForm):
    class Meta:
        model = Post
        template_name = 'newpost.html'
        fields = ['author', 'title']

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
        }
