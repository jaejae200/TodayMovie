from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
import requests

# Create your views here.

def signup(request):
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            user = sigup_form.save()
            login(request, user)
    else:
        sigup_form = CustomUserCreationForm()

    context = {
        'signup_form' : signup_form, 
    }

    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            login(request, login_form.get_user())
    
    else:
        login_form = AuthenticationForm()

    context = {
        'login_form' : login_form
    }

    return render(request, 'accounts/login.html', context)

def logout(request):
    
    logout(request)

    return redirect('articles:index')
