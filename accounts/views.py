from django.shortcuts import render
from django.contrib.auth import login
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
