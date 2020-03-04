from django.http import HttpResponse
from django.shortcuts import render

def hello2(request):
    return HttpResponse("Hello world!")

def hello(request):
    context = {}
    
    context['hello'] = 'hello world22222 !'
    return render(request,"hello.html",context)