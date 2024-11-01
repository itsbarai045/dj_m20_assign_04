from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import models

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username",'class':'border rounded border-solid border-slate-300'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", 'class':'border rounded border-solid border-slate-300'}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['mobile_number', 'address', 'website']
        widgets = {
            'mobile_number':forms.TextInput(attrs={'placeholder': 'Mobile Number'}),
            'address':forms.Textarea(attrs={'placeholder': 'Address', 'rows': 3}),
            'website':forms.TextInput(attrs={'placeholder': 'Website'}),
        }