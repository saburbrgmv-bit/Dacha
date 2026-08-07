from django.urls import path
from .views import *

urlpatterns = [
  path('', CottageListView.as_view(), name='cottage_list'),
  path('create/', CottageCreateView.as_view(), name='cottage_create'),
  path('update/<int:pk>/', CottageUpdateView.as_view(), name='cottage_update'),
  path('delete/<int:pk>/', CottageDeleteView.as_view(), name='cottage_delete'),
  path('detail/<int:pk>/', CottageDetailView.as_view(), name='cottage_detail'),
]