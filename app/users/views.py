from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import RegisterForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import CreateView

def home(request):
  return render(request, "users/home.html")

class RegisterView(CreateView):
  form_class = RegisterForm
  template_name = "users/register.html"
  success_url = reverse_lazy('home')

class SignView(LoginView):
  template_name = 'users/login.html'
  success_url = reverse_lazy('cottage_list')


def exit(request):
  logout(request)
  return redirect('login')