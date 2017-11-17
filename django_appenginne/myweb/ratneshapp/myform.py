#-*- coding: utf-8 -*-
from django import forms
from ratneshapp.models import Register
class LogonForm(forms.Form):
	user = forms.CharField(max_length=50)
	mail = forms.CharField(max_length = 50)
	phonenumber = forms.IntegerField()
	password = forms.CharField(widget=forms.PasswordInput())
	picture = forms.FileField()

class LoginForm(forms.Form):
	user = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput())
	
