from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxValueValidator
from .models import Profile


class UserRegistraterForm(UserCreationForm):
	email = forms.EmailField()
	phone_number=forms.IntegerField()

	class Meta:
		"""docstring for Meta"""
		model = User
		fields = ['username','email','password1','password2','phone_number']

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','email']

	
class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']