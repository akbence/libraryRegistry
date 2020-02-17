from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class QueryForm(forms.Form):
    title = forms.CharField(label='Title', required=False)
    category = forms.CharField(label='Category', required=False)
    author = forms.CharField(label='Author', required=False)
    only_read = forms.BooleanField(label="Only read", required=False)
