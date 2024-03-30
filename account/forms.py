from django import forms
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm, UsernameField, 
                                       PasswordChangeForm, PasswordResetForm, SetPasswordForm)
                                      
from django.contrib.auth.models import User


class CustomerRegisterationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Enter Password Again', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    class  Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        widgets = {'username':forms.TextInput(attrs={'autofocues':True, 'class':'form-control'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocues':True, 'class':'form-control'}))
    password = forms.CharField(label='Password', strip=False, 
                               widget=forms.PasswordInput(attrs={'autofocues':True, 'class':'form-control'}))
    
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs=
                    {'autofocues':True, 'autocomplete': 'current-password','class':'form-control'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs=
                    {'autofocues':True, 'autocomplete': 'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs=
                    {'autofocues':True, 'autocomplete': 'current-password','class':'form-control'}))



class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs=
                    { 'autocomplete': 'email','class':'form-control'}))
    
class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs=
                    {'autofocues':True, 'autocomplete': 'new-password','class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs=
                    {'autofocues':True, 'autocomplete': 'new-password','class':'form-control'}))