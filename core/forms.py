from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'appointment_date', 'appointment_time', 'status', 'notes']

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Username',
        'class': 'form-control'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter Password",
        "class": "form-control"
    }))

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username =forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Username',
        'class': 'form-control'
    }))
    email =forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter Password",
        "class": "form-control"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Repeat Password",
        "class": "form-control"
    }))

