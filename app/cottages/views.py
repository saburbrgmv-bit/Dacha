from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import CottageForm
from .models import Cottage


class CottageListView(ListView):
  model = Cottage
  template_name = 'cottage/cottage_list.html'
  context_object_name = 'cottages'

class CottageCreateView(CreateView):
  model = Cottage
  form_class = CottageForm
  template_name = 'cottage/cottage_create.html'
  success_url = reverse_lazy('cottage_list')