from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")

def test(request):
    return HttpResponse("Test Me")