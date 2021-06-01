from django import forms

from .models import Mathematician, Country, University, MathSubjectClass, StudentAdvisor, ArticleMathematician, \
    MagazineArticle, Article, Magazine
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


class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = '__all__'
        widgets = {
            'country_name': TextInput(attrs={
                'class': 'form-control'
            })
        }


class UniversityForm(ModelForm):
    class Meta:
        model = University
        fields = '__all__'
        widgets = {
            'university_name': TextInput(attrs={
                'class': 'form-control'
            })
        }


class MathSubjectClassForm(ModelForm):
    class Meta:
        model = MathSubjectClass
        fields = '__all__'
        widgets = {
            'math_subject_class_name': TextInput(attrs={
                'class': 'form-control'
            })
        }


class StudentAdvisorForm(ModelForm):
    class Meta:
        model = StudentAdvisor
        fields = '__all__'
        widgets = {
            'student': Select(attrs={
                'class': 'form-control ntSaveForms'
            }),
            'advisor': Select(attrs={
                'class': 'form-control ntSaveForms'
            })
        }


class ArticleMathematicianForm(ModelForm):
    class Meta:
        model = ArticleMathematician
        fields = '__all__'
        widgets = {
            'article': Select(attrs={
                'class': 'form-control'
            }),
            'mathematician': Select(attrs={
                'class': 'form-control'
            })
        }


class MagazineArticleForm(ModelForm):
    class Meta:
        model = MagazineArticle
        fields = '__all__'
        widgets = {
            'article': Select(attrs={
                'class': 'form-control'
            }),
            'magazine': Select(attrs={
                'class': 'form-control'
            })
        }


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'article_name': TextInput(attrs={
                'class': 'form-control'
            }),
            'year': NumberInput(attrs={
                'class': 'form-control'
            })
        }


class MagazineForm(ModelForm):
    class Meta:
        model = Magazine
        fields = '__all__'
        widgets = {
            'magazine_name': TextInput(attrs={
                'class': 'form-control'
            }),
            'year': NumberInput(attrs={
                'class': 'form-control'
            })
        }
