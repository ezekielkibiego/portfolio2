
from django.forms.widgets import Textarea
from .models import *
from django.forms import ModelForm
from django import forms

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields =['name','email', 'message' ]
        widgets = {
            'message': Textarea(attrs={'cols' : 20, 'rows' : 3}),
        }