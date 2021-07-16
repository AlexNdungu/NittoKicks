from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Products


#Registration Form

class createUserForm(UserCreationForm):

    password2 = None

    class Meta:
        model = User
        fields = ['username','email','password1']

class addProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
