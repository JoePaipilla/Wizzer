from django import forms
from django.contrib.auth.models import User


class WhizForm(forms.Form):
    whiz_input = forms.CharField(label="", widget=forms.Textarea(attrs={"cols": '',"rows": '',"id": "message","placeholder":"Write a post!","value": "message"}))


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']