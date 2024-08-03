"""Create Forms for Authentication"""

from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create Authentication Form
class LoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

        def __init__(self, *args, **kwargs):
            super(RegistrationForm, self).__init__(*args, **kwargs)
            self.fields['username'].widget.attrs.update({'class': 'username'})
            self.fields['password1'].widget.attrs.update({'class': 'password'})


# Create Registration Form
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

        def __init__(self, *args, **kwargs):
            super(RegistrationForm, self).__init__(*args, **kwargs)
            self.fields['email'].widget.attrs.update({'class': 'email'})
            self.fields['username'].widget.attrs.update({'class': 'username'})
            self.fields['password1'].widget.attrs.update({'class': 'password1'})
            self.fields['password2'].widget.attrs.update({'class': 'password2'})
