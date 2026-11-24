from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    agree = forms.BooleanField(error_messages={'required': 'Please accept the terms.'})

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()
        if User.objects.filter(username=email).exists():
            raise forms.ValidationError('Email already in use.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # email is the login name
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['full_name']
        if commit:
            user.save()
        return user