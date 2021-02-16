from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Profile
from cloudinary.forms import CloudinaryFileField

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        
        
class SignupForm(UserCreationForm):
    username=forms.CharField(label='사용자명',widget=forms.TextInput(attrs={
        'pattern':'[a-zA-Z0-9]+',
        'title' : '특수분자, 공백 입력불가',
    }))
    nickname=forms.CharField(label="닉네임")
    picture=CloudinaryFileField(options = {
            'crop': 'thumb',
            'width': 150,
            'height': 150,
            'folder': 'picture'
       })
    
    class Meta(UserCreationForm.Meta):
        UserCreationForm.Meta.fields + ('email',)
        
    def clean_nickname(self):
        nickname=self.cleaned_data.get('nickname')
        if Profile.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError('이미 존재하는 닉네임입니다.')
        return nickname
    
    def clean_email(self):
        email=self.cleaned_data.get('email')
        User=get_user_model()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('사용중인 이메일 입니다.')
        return email
    
    def clean_picture(self):
        picture=self.cleaned_data.get('picture')
        if not picture:
            picture = None
        return picture
    
    def save(self):
        user=super().save()
        Profile.objects.create(
        user=user,
        nickname=self.cleaned_data['nickname'],
        picture=self.cleaned_data['picture']
        )
        return user