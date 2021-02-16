from django.contrib import admin
from .models import Profile,Follow

# Register your models here.
class FollowInline(admin.TabularInline):
    model=Follow
    fk_name = 'from_user'


@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ['id', 'nickname', 'user']
    list_display_links = ['nickname', 'user']
    search_field = ['nickname']
    inlines=[FollowInline]
    
@admin.register(Follow)
class Follow(admin.ModelAdmin):
    list_display = ['from_user','to_user','created_at']
    list_display_links = ['from_user','to_user','created_at']