from django import forms
from django.contrib.auth.models import User
from pollsnew import models as pollsnew_models

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model=User
		
		fields=('username','email','password','first_name','last_name')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model=pollsnew_models.UserProfile
		fields=('website','picture')
		#or we can write instead of fields	
		#exclude=('picture')
	