from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
def homepage(request:HttpRequest) -> HttpResponse:
    page_title = "Home Page"
    return render(request, "index.html",{'title':page_title})

def about(request:HttpRequest) -> HttpResponse:
    return render(request, "about.html",{})

def contact(request:HttpRequest) -> HttpResponse:
    return render(request, "contact.html",{})