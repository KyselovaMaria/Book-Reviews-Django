from django import forms
from .models import BookSearch, Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BookSearchForm(forms.ModelForm):
    name_of_book = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': "form-control me-2", 'placeholder': 'Enter name of book'
    }))
    class Meta:
        model = BookSearch
        fields = ['name_of_book',]

class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={
        'class' : 'form-control', 'placeholder': 'Enter Username'
    }))

    email = forms.CharField(max_length = 100, widget = forms.EmailInput(attrs={
        'class' : 'form-control', 'placeholder': 'Enter Email Address'
    }))

    password1 = forms.CharField(max_length = 100, widget = forms.PasswordInput(attrs={
        'class' : 'form-control', 'placeholder': 'At least eight characters'
    }))
    password2 = forms.CharField(max_length = 100, widget = forms.PasswordInput(attrs={
        'class' : 'form-control', 'placeholder': 'Confirm Password'
    }))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RatingForm(forms.Form):
    rating = forms.IntegerField(
        label='Rating',
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','slug', 'cover_image', 'author', 'summary',
                  'author_summary', 'category', 'recommended_books',
                  'ukrainian_books', 'bestsellers_books', 'average_rating']