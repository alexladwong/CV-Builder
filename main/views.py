from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from main import forms


# from main import settings
# from django.core.mail import send_mail, user

# Create your views here.



@login_required(login_url='/login')
def home(request):
    return render(request, 'main/home.html')

@login_required(login_url="login")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect("/home")
        else:
            form = PostForm()

            subject = forms.CharField(max_length=50)
        return render(request, "main/create_post.html", {"form": form})
    
    


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
           
            return redirect('/index')
    else:
        form = RegisterForm()    

        
    return render(request, 'registration/sign_up.html', {"form":form})


def index(request):
    return render(request, 'main/index.html')

def resume(request):
    return render(request, 'main/resume.html')


def post(request):
    return render(request, 'registration/create_post.html')

def CV(request):
    return render(request, 'main/CV.html')
