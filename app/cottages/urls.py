from django.urls import path
from .views import *

urlpatterns = [
  path('', CottageListView.as_view(), name='cottage_list'),
  path('create/', CottageCreateView.as_view(), name='cottage_create'),
]