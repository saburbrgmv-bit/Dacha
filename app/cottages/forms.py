from django import forms
from .models import Cottage

class CottageForm(forms.ModelForm):
  class Meta:
    model = Cottage
    fields = ['name', 'location', 'avatar', 'content', 'price']