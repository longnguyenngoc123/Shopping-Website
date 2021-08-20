from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import fields
from django.forms.models import ModelFormMetaclass
from django.utils.safestring import mark_safe
from .models import Profile
class Register(forms.Form):
    username = forms.CharField(max_length=30,label='',widget=forms.TextInput(attrs={'placeholder': 'Account'}))
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    repassword = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter Password'}))

    def clean_repassword(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            repassword = self.cleaned_data['repassword']
            if password==repassword and password:
                return repassword
        raise forms.ValidationError("Password enterd not suit with the password")
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Special character doesn't allow")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Account already exist")
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password'])
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User  
        fields = ['email','is_staff']   
class UserAddForm(forms.ModelForm):
    class Meta:
        model = User  
        fields ='__all__'          
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile  
        fields = ['name','birth_date','phone','image']   

class AddUserForm(forms.Form):
    username = forms.CharField(max_length=30,label='',widget=forms.TextInput(attrs={'placeholder': 'Account'}))
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password'])
