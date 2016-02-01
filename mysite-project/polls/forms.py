from .models import ContactForm
from django import forms

class ContactForm1(forms.ModelForm):
	class Meta:
		model=ContactForm
		fields=('name',)
		
		
		