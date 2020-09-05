"""
Create new forms that inherit from UserCreationForm but with the views and fields we want like email etc.
"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Listing

class LostRegisterForm(forms.ModelForm):
    
    class Meta:
        """Gives us a nested name space for a configuration and
        says that the models that are going to be affected are the user models
        and the fields that we want are in this list"""
        model = Listing
        fields = ['Title', 'Date', 'Place', 'Image', 'Description']  


class ListingUpdateForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['Title', 'Image', 'Description']

class FoundRegisterForm(forms.ModelForm):
    
    class Meta:
        model = Listing
        fields = ['Title', 'Date', 'Place', 'Image', 'Description']  


class FoundUpdateForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['Title', 'Image', 'Description']