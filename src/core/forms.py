from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Brugernavn', max_length=254)
    password = forms.CharField(label='Kode', widget=forms.PasswordInput)


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Brugernavn', max_length=254)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Kode'
        self.fields['password2'].label = 'Bekræft kode'
        self.fields['password1'].help_text = (
            "Din adgangskode skal indeholde mindst 8 tegn.<br>"
            "Din adgangskode må ikke være en almindeligt brugt adgangskode.<br>"
            "Din adgangskode må ikke udelukkende bestå af tal."
        )
        self.fields['password2'].help_text = (
            "Gentag venligst koden."
        )