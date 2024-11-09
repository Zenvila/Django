from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is Homepage ")


def about(request):
    return HttpResponse("hello  ! About ")

def services(request):
    return HttpResponse( "Services Page  ")


def contact(request):
    return HttpResponse( "Contact Page  ")