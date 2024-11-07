from django.http import HttpResponse
def home(request):
    return HttpResponse("Django Home Page")

def about(request):
    return HttpResponse("Django About Page")

def contact(request):
    return HttpResponse("Django Contact Page")