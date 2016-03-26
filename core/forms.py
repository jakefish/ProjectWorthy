from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

    class Meta:
        
        model = User
        fields = ('email','username', 'password')
