from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
	username = forms.EmailField(max_length=254, label='Email address', help_text='Required. Inform a valid email address')

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', )