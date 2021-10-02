from django.shortcuts import render

# Create your views here.

def index(request):
    variales = {
        'name' : 'yousef'
    }
    return render(request,'pages/index.html',variales)

def about(request):
    return render(request,'pages/about.html')