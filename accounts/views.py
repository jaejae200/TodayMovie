from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm
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

def detail(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    
    context = {
        'user': user
    }

    return render(request, 'accounts/detail.html', context)

@login_required
def update(request):
    if request.method == 'POST':
        update_form = CustomUserChangeForm(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            return redirect('accounts:detail', request.user.pk)
    else:
        update_form = CustomUserChangeForm(instance=request.user)
    
    context = {
        'update_form': update_form
    }
    
    return render(request, 'accounts/update.html', context)
