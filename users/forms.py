"""
Create new forms that inherit from UserCreationForm but with the views and fields we want like email etc.
"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # default is required true anyway
    class Meta:
        """Gives us a nested name space for a configuration and
        says that the models that are going to be affected are the user models
        and the fields that we want are in this list"""
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # pass2 is confirmation password


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']