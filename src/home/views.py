from django.shortcuts import render
from django.views import generic
from reference import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

#Homepage
class HomePage(generic.ListView):
    model = models.Title
    template_name = 'home/homepage.html'

class EditPage(LoginRequiredMixin, generic.ListView):
    model = models.Title
    template_name = 'home/edit.html'
    login_url = reverse_lazy('roles:login')

class AboutPage(generic.TemplateView):
    template_name = 'home/about.html'

class ProfilePage(LoginRequiredMixin, generic.TemplateView):
    template_name = 'home/profile.html'
    login_url = reverse_lazy('roles:login')
