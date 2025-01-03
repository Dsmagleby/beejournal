from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Brugernavn', max_length=254)
    password = forms.CharField(label='Kode', widget=forms.PasswordInput)