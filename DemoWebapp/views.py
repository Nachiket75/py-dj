from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def courses(request):
    return  HttpResponse('<h1>This is my Home page</h1')