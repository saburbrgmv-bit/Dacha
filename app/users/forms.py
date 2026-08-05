from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
  phone = forms.CharField(max_length=50)
  email = forms.EmailField()
  username = forms.CharField(max_length=200)
  password = forms.CharField(max_length=200)

  class Meta:
    model = User
    fields = ['username', 'email', 'phone', 'password']