from django.shortcuts import render, redirect

def prueba(request):
    return render(request, 'mapjs\\home.html')

# Create your views here.
