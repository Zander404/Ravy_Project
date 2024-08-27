from .models import User, Post, Role, Category
from django import forms


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'



class RoleForm(forms.ModelForm):

    class Meta:
        model = Role
        fields = '__all__'


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


