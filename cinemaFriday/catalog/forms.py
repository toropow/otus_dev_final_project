from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


# class AnimalForm(forms.ModelForm):
#     name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#
#     class Meta:
#         model = Animal
#         exclude = ('user',)


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='firstname', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='lastname', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')


class LoginForm(AuthenticationForm):
    class Meta:
        fields = '__all__'
