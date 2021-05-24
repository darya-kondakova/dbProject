from django import forms

from .models import Mathematician
from django.forms import ModelForm, TextInput, Select, NumberInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserSignInForm(AuthenticationForm):
    username = forms.CharField(help_text="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Name'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))


class UserSignUpForm(UserCreationForm):
    username = forms.CharField(help_text="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Name'}))
    email = forms.EmailField(help_text="", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email address'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}


class MathematicianForm(ModelForm):
    class Meta:
        model = Mathematician
        fields = '__all__'
        widgets = {
            'last_name': TextInput(attrs={
                'class': 'form-control'
            }),
            'middle_mane': TextInput(attrs={
                'class': 'form-control'
            }),
            'first_name': TextInput(attrs={
                'class': 'form-control'
            }),
            'year_of_degree': NumberInput(attrs={
                'class': 'form-control'
            }),
            'university_id': Select(attrs={
                'class': 'form-control'
            }),
            'country_id': Select(attrs={
                'class': 'form-control'
            }),
            'math_subject_class_id': Select(attrs={
                'class': 'form-control'
            })
        }
