from django.shortcuts import render
from django.views import generic
from reference import models as refmod
from cart import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.

#Homepage
class HomePage(generic.ListView):
    model = refmod.Title
    template_name = 'home/homepage.html'

class EditPage(LoginRequiredMixin, generic.ListView):
    model = refmod.Title
    template_name = 'home/edit.html'
    login_url = reverse_lazy('roles:login')

class AboutPage(generic.TemplateView):
    template_name = 'home/about.html'

class ProfilePage(LoginRequiredMixin, generic.TemplateView):
    template_name = 'home/profile.html'
    login_url = reverse_lazy('roles:login')
    
