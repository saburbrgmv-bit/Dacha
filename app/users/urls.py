from django.urls import path
from .views import *

urlpatterns = [
  path("", home, name="home"),
  path('register/', RegisterView.as_view(), name="register"),
  path('login/', SignView.as_view(), name="login"),
  path("logout/", exit, name="logout"),
]