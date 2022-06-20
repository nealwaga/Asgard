from django import forms
from .models import *


#Create forms here

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['profile_picture','bio','email','phone_number'] 
        
class HoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        fields=['name','location','description','image']         
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title','info']       
        
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields=['image','name','email','phone_number']            
        
           