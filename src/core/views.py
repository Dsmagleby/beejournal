from django.contrib.auth.views import LoginView 
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from core.forms import CustomAuthenticationForm, CustomUserCreationForm


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')