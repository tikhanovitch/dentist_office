from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserPersonalAccount, Appointment


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class UserPersonalAccountForm(forms.ModelForm):
    class Meta:
        model = UserPersonalAccount
        fields = ["first_name", "last_name", "phone_number", "photo"]


class AddUserPersonalAccountForm(forms.ModelForm):
    class Meta:
        model = UserPersonalAccount
        fields = ["first_name", "last_name", "phone_number", "photo"]


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'description']
