from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    # phone_number = forms.CheckboxInput(required=True)

    class Meta:
        model = User
        fields = ["username", "first_name",  "email", "password1", "password2"]

        # widgets = {
        #     'username': forms.Textarea(attrs={'class': 'input-group mb-3'}),
        #     'first_name': forms.Textarea(attrs={'class': 'input-group mb-3'}),
        #     'email': forms.TextInput(attrs={'class': 'input-group mb-3'}),
        #     'password1': forms.TextInput(attrs={'class': 'input-group mb-3'}),
        #     'password2': forms.TextInput(attrs={'class': 'input-group mb-3'}),

        # }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # field_class = RegisterForm
        fields = ["title", "description"]





