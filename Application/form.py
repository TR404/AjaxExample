from django import forms
from .models import *

class IntroForm(forms.ModelForm):
	class Meta:
		model = Intro
		fields = ['name', 'mobile', 'email', 'about']
		widgets = {
			'name' : forms.TextInput(attrs = {'class' : 'form-control', 'id': 'nameId'}),
			'mobile' : forms.TextInput(attrs = {'class' : 'form-control', 'id': 'mobileId'}),
			'email' : forms.TextInput(attrs = {'class' : 'form-control', 'id': 'emailId'}),
			'about' : forms.TextInput(attrs = {'class' : 'form-control', 'id': 'aboutId'}),
		}
