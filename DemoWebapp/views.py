from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return  HttpResponse('<h1>This is my Home page</h1')
    return  render(request,'home.html', {'name':'Nachiket'})

def add(request):
    no1=int( request.GET['num1'])
    no2=int( request.GET['num2'])
    result = no1+no2
    return render(request, 'result.html',{'result':result})
