from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'suwapp/home.html', {})

def ranked(request):
    return render(request, 'suwapp/ranked.html', {})

def compensation(request):
    return render(request, 'suwapp/compensation.html', {})        
