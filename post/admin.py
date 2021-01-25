from django.contrib import admin
from django import forms
from .models import Post
# Register your models here.


class PostForm(forms.ModelForm):
    content =forms.CharField(widget = forms.Textarea)
    class Meta:
        model=Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','author','nickname','content','created_at']
    list_display_link =['author','nickname','content']
    form=PostForm
    def nickname(request,post):
        return post.author.profile.nickname