from django.shortcuts import render
from django.views import generic
from reference import models

# Create your views here.

#Homepage
class HomePage(generic.ListView):
    model = models.Title
    template_name = 'home/homepage.html'