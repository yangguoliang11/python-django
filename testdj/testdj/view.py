from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world!")

def hello2(request):
    return HttpResponse("Hello world2!")