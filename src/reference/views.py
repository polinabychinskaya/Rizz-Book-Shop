from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

#List all genres
def view_genre(request):
    genre = models.Genre.objects.all()
    return render(request, 
                  template_name='reference/allgenres.html', 
                  context={'objgenre': genre})

#List all titles
def view_titles(request):
    title = models.Title.objects.all()
    return render(request, 
                  template_name='reference/alltitles.html', 
                  context={'objtitle': title})

#List all authors
def view_authors(request):
    author = models.Author.objects.all()
    return render(request, 
                  template_name='reference/allauthors.html', 
                  context={'objauthor': author})

#List all editions
def view_editions(request):
    edition = models.Edition.objects.all()
    return render(request, 
                  template_name='reference/alleditions.html', 
                  context={'objedition': edition})

#List all publishing houses
def view_publishing_houses(request):
    publishing_house = models.PublishingHouse.objects.all()
    return render(request, 
                  template_name='reference/allpublishinghouses.html', 
                  context={'objpublish': publishing_house})