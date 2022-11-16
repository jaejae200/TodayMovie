from django.shortcuts import render
import requests

# Create your views here.

def signup(request):
    return render(request, 'accounts/signup.html')