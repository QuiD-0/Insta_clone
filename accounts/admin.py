from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ['id', 'nickname', 'user']
    lsit_display_links = ['nickname', 'user']
    search_field = ['nickname']