from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Green Bank!")