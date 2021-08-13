from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserSignupForm(UserCreationForm):
    email=forms.EmailField(required=True, 
    help_text='Enter a valid email as name@domain.ext')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        # # this will create a form for all the data fields in the User model
        # fields = "__all__" 

class InputForm(forms.Form):
    first_name=forms.CharField()
    las_name=forms.CharField()
