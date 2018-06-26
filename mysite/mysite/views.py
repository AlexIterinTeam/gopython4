from django.http import HttpResponse

def helloworld(request):
    return HttpResponse('<html><head></head><body>Hello world!</body></html>')