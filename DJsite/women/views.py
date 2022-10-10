from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


# Create your views here.
def index(request): # reference to http//
    return HttpResponse("The page of women application")

def categories (request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1> Article by categories </h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True) # Shold allways use '/' implicit address
    return HttpResponse(f"<h1> Archive by years</h1><p>{year}</p>")

def pageNotFound(request, excpetion):
    return HttpResponseNotFound('<h1> The page is not found</h>')
