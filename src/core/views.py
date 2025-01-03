from django.contrib.auth.views import LoginView
from core.forms import CustomAuthenticationForm


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm