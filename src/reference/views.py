from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.views import generic


# Create your views here.

#---------GENRES SECTION---------#

#List all genres
class GenreListView(generic.ListView):
    model = models.Genre
    template_name = 'reference/allgenres.html'

#Create a new genre
class GenreCreateView(generic.CreateView):
    model = models.Genre
    fields = [
        'name', 'description'
    ]
    template_name = 'reference/creategenre.html'

#Update the genre
class GenreUpdateView(generic.UpdateView):
    model = models.Genre
    fields = [
        'name', 'description'
    ]
    template_name = 'reference/updategenre.html'

#Delete the genre
class GenreDeleteView(generic.DeleteView):
    model = models.Genre
    template_name = 'reference/deletegenre.html'
    success_url = '/success'

#---------TITLES SECTION---------#

#Book details
class TitleDetailView(generic.DetailView):
    model = models.Title
    template_name='reference/productdetails.html'

#List all titles
class TitleListView(generic.ListView):
    model = models.Title
    template_name='reference/alltitles.html'

#Create a new title
class TitleCreateView(generic.CreateView):
    model = models.Title
    fields = [
        'picture', 'book_title', 'price', 'author', 'edition', 'genre', 'publishing_house', 'description'
    ]
    template_name = 'reference/createtitle.html'

#Update the title
class TitleUpdateView(generic.UpdateView):
    model = models.Title
    fields = [
        'book_title', 'price', 'author', 'edition', 'genre', 'publishing_house', 'description'
    ]
    template_name = 'reference/updatetitle.html'

#Delete the title
class TitleDeleteView(generic.DeleteView):
    model = models.Title
    template_name = 'reference/deletetitle.html'
    success_url = '/success'

#---------AUTHORS SECTION---------#

#List all authors
class AuthorListView(generic.ListView):
    model = models.Author
    template_name='reference/allauthors.html'

#Create a new author
class AuthorCreateView(generic.CreateView):
    model = models.Author
    fields = [
        'name', 'language'
    ]
    template_name = 'reference/createauthor.html'

#Update the author
class AuthorUpdateView(generic.UpdateView):
    model = models.Author
    fields = [
        'name', 'language'
    ]
    template_name = 'reference/updateauthor.html'

#Delete the author
class AuthorDeleteView(generic.DeleteView):
    model = models.Author
    template_name = 'reference/deleteauthor.html'
    success_url = '/success'

#---------EDITIONS SECTION---------#

#List all editions
class EditionListView(generic.ListView):
    model = models.Edition
    template_name='reference/alleditions.html'

#Create a new edition
class EditionCreateView(generic.CreateView):
    model = models.Edition
    fields = [
        'number'
    ]
    template_name = 'reference/createedition.html'

#Update the edition
class EditionUpdateView(generic.UpdateView):
    model = models.Edition
    fields = [
        'number'
    ]
    template_name = 'reference/updateedition.html'

#Delete the edition
class EditionDeleteView(generic.DeleteView):
    model = models.Edition
    template_name = 'reference/deleteedition.html'
    success_url = '/success'

#---------PUBLISHING HOUSES SECTION---------#

#List all publishing houses
class PublishingHouseListView(generic.ListView):
    model = models.PublishingHouse
    template_name='reference/allpublishinghouses.html'

#Create a new publishing house
class PublishingHouseCreateView(generic.CreateView):
    model = models.PublishingHouse
    fields = [
        'name', 'country'
    ]
    template_name = 'reference/createpublishinghouse.html'

#Update the publishing house
class PublishingHouseUpdateView(generic.UpdateView):
    model = models.PublishingHouse
    fields = [
        'name', 'country'
    ]
    template_name = 'reference/updatepublishinghouse.html'

#Delete the publishing house
class PublishingHouseDeleteView(generic.DeleteView):
    model = models.PublishingHouse
    template_name = 'reference/deletepublishinghouse.html'
    success_url = '/success'

#---------SUCCESS PAGE---------#

def success_page(request):
    return render(
        request,
        template_name='reference/success.html'
    )