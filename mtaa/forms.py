from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

#Create forms here
class CreateHoodForm(forms.ModelForm):

	class Meta:
		model = Hood
		exclude = ['user','occupants_count']
  
  
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'business','email','u_hood']