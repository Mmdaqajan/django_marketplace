from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from core.models import Item


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email',
        'class': 'w-full py-4 px-6 rounded-xl'

    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'w-full py-4 px-6 rounded-xl'

    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat Password',
        'class': 'w-full py-4 px-6 rounded-xl'

    }))


class LoginFrom(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'w-full py-4 px-6 rounded-xl'

    }))


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')

        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'price': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border',
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border',
            })
        }
