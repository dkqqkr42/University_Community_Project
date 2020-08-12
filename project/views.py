from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signin(request):
    return render(request, 'signin.html')