from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

#Create forms here
class CreateHoodForm(forms.ModelForm):

	class Meta:
		model = Hood
		exclude = ['user','occupants_count']