from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from . import models

# Create your views here.

class LoginView(auth_views.LoginView):
    template_name = 'roles/login.html'

class LogoutView(auth_views.LogoutView):
    template_name = 'roles/logout.html'

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/success'
    template_name = 'roles/signup.html'




    