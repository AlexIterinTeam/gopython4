from django.http import HttpResponse
from django.shortcuts import render
from mysite.settings import STATIC_ROOT

def helloworld(request):
    return HttpResponse('<html><head></head><body>Hello world!</body></html>')


def mainpage(request):
    return render(request, 'mainpage.html')