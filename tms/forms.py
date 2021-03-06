from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', max_length=254, help_text='Required. Enter a valid email address.')
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username','email', 'first_name','last_name','password1','password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']