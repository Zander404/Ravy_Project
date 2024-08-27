from django.forms import TextInput

from .models import User, Post, Role, Category
from django import forms

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'class': 'w-96 form-control input border border-black',
            'placeholder': 'Enter your username',
            'style': 'background-color: #f9f9f9; border-radius: 5px;',
        })
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'w-96 form-control input border border-black',  # Adicione aqui suas classes CSS personalizadas
            'placeholder': 'Enter your email',  # Adicione um placeholder, se desejar
            'style': 'background-color: #f9f9f9; border-radius: 5px;',  # Estilos inline, se necessário
        })
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-96 form-control input border border-black',
            'placeholder': 'Enter your password',
            'style': 'background-color: #f9f9f9; border-radius: 5px;',
        })
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-96 form-control input border border-black',
            'placeholder': 'Confirm your password',
            'style': 'background-color: #f9f9f9; border-radius: 5px;',
        })
    )


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        exclude = ['usable_password']

    def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.help_text = None  # Remove o help text de todos os campos


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-96 form-control input border border-black'}),
            'description': forms.Textarea(attrs={'class': 'form-control textarea border border-black'}),
            'content': forms.Textarea(attrs={'class': 'form-control textarea border border-black'}),
            'posted_by': forms.Select(attrs={'class': 'text-black select gap-4 w-full max-w-xs '}),
            'banner': forms.FileInput(attrs={'class': "file-input  w-full max-w-xs"})
        }


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
