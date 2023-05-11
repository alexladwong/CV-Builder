from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput, EmailInput


# Create your models here.




class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    degree = models.TextField(max_length=100)
    skills = models.TextField(max_length=100)
    experience = models.TextField(max_length=100)
    previous_work = models.TextField(max_length=100)
    about_you = models.TextField(max_length=100)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)   
    description = models.TextField(200) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.title + "\n" + self.description    

class UserInfoForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 100px;', 'class': 'form-control'}))
