from django.forms import ModelForm
from .models import Book
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Page_Two(ModelForm):
    class Meta:
        model = Book
        fields = ['nazwa', 'opis', 'gatunek', 'cena', 'rok_wydania', 'autor', 'zdjecie', 'przecena']

        # fileds mają być uzyte w naszym forms
        # exclude mają być wykluczone


class UserRegisterForm(UserCreationForm):
     email = forms.EmailField()

     class Meta:
         model = User
         fields = ['username', 'email', 'password1', 'password2']