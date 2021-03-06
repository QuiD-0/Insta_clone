from django.contrib import admin
from django import forms
from .models import Post,Like,Bookmark,Comment
# Register your models here.


class PostForm(forms.ModelForm):
    content =forms.CharField(widget = forms.Textarea)
    class Meta:
        model=Post
        fields = '__all__'

class LikeInline(admin.TabularInline):
    model = Like
    
    
class CommentInline(admin.TabularInline):
    model = Comment
    
        

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','author','nickname','content','created_at']
    list_display_link =['author','nickname','content']
    form=PostForm
    inlines = [CommentInline,LikeInline]
    def nickname(request,post):
        return post.author.profile.nickname
    
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display=['id','post','user','created_at']
    list_display_link = ['post','user']



@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display=['id','post','user','created_at']
    list_display_link = ['post','user']
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['post','content','author','created_at']
    list_display_link = ['post','content','author']
    
    
    
    
    
    
    
    