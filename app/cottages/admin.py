from django.contrib import admin
from .models import Cottage

@admin.register(Cottage)
class CottageAdmin(admin.ModelAdmin):
  list_display = ['name', 'content']