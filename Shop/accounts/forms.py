from django import forms
from .models import Account


class LoginForm(forms.Form):

        email = forms.EmailField()
        password = forms.CharField(widget = forms.PasswordInput())

class SignUpForm(forms.Form):

        email = forms.EmailField()
        password = forms.CharField(widget=forms.PasswordInput())
        repeat_password = forms.CharField(widget=forms.PasswordInput())