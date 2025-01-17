from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=[('Admin', 'Admin'), ('Alumni', 'Alumni'), ('Student', 'Student')])

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'password1', 'password2']

    # #Custom validation (e.g., email domain checks)
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not email.endswith("@yourinstitution.edu"):
    #         raise forms.ValidationError("Please use your institutional email address.")
    #     return email