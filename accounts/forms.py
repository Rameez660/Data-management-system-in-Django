from django.forms import ModelForm
from .models import Order
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

# class CreateUserForm(forms.ModelForm):
	

# 	# class meta:
# 	# 	model = User
# 	# 	fields = ['username','email','password1','password2']

# 	username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'},required=True, max_length=50)
# 	# email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'},required=True, max_length=50)/	
# 	# firstname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First name'},required=True, max_length=50)
# 	# lastname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'},required=True, max_length=50)
# 	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'},required=True, max_length=50)
# 	confirmpassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'},required=True, max_length=50)
# 	class meta:
# 		model = User
# 		fields = ['username','password','password2']
