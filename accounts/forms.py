from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'bio', 'profile_picture')

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if phone == '':
            return None
        return phone

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'bio', 'profile_picture')
