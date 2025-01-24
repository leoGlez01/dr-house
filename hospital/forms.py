from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=15, required=False)
    role = forms.ChoiceField(choices=[('patient', 'Paciente'), ('doctor', 'Doctor')], required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'full_name', 'phone_number', 'role', 'password1', 'password2')