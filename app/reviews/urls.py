from django.urls import path
from .views import *

urlpatterns = [
  path('', ReviewListView.as_view(), name="review_list"),
  path('create/', ReviewCreateView.as_view(), name="review_create"),
  path('updat/<int:pk>/', ReviewUpdateView.as_view(), name="review_update"),
  path('delete/<int:pk>/', ReviewDeleteView .as_view(), name="review_delete"),
]