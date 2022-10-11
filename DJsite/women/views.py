from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(request): # reference to http//request
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'menu': menu, 'title':'Главная страница', 'posts': posts} )

def about(request): # reference to http//request
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})

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
