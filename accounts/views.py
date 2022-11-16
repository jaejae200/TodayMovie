from django.shortcuts import render
from django.contrib.auth import login
from .forms import CustomUserCreationForm
import requests

# Create your views here.

def signup(request):
    if request.method == 'POST':
        sigup_form = CustomUserCreationForm(request.POST)
        if sigup_form.is_valid():
            user = sigup_form.save()
            login(request, user)
    else:
        sigup_form = CustomUserCreationForm()
        
    return render(request, 'accounts/signup.html')