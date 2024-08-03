from .forms import LoginForm, RegistrationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .models import User
from django.shortcuts import render

__all__ = ['RegistrationView', 'LoginUserView', 'home', 'subscriptions']


# View for Registration
class RegistrationView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = '/'


# View for Login
class LoginUserView(LoginView):
    model = User
    template_name = 'login.html'
    form_class = LoginForm
    redirect_authenticated_user = True


# Create a home page
def home(request):
    return render(request, 'home.html')


# Create Subscriptions page (just how much cost the subscriptions)
def subscriptions(request):
    return render(request, 'subscriptions.html')
