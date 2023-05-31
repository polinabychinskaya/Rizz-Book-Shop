"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reference import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view()),
    path('allgenres/', views.GenreListView.as_view()),
    path('creategenre/', views.GenreCreateView.as_view()),
    path('updategenre/<int:pk>', views.GenreUpdateView.as_view()),
    path('deletegenre/<int:pk>', views.GenreDeleteView.as_view()),
    path('alltitles/', views.TitleListView.as_view()),
    path('createtitle/', views.TitleCreateView.as_view()),
    path('updatetitle/<int:pk>', views.TitleUpdateView.as_view()),
    path('deletetitle/<int:pk>', views.TitleDeleteView.as_view()),
    path('allauthors/', views.AuthorListView.as_view()),
    path('createauthor/', views.AuthorCreateView.as_view()),
    path('updateauthor/<int:pk>', views.AuthorUpdateView.as_view()),
    path('deleteauthor/<int:pk>', views.AuthorDeleteView.as_view()),
    path('alleditions/', views.EditionListView.as_view()),
    path('createedition/', views.EditionCreateView.as_view()),
    path('updateedition/<int:pk>', views.EditionUpdateView.as_view()),
    path('deleteedition/<int:pk>', views.EditionDeleteView.as_view()),
    path('allpublishinghouses/', views.PublishingHouseListView.as_view()),
    path('createpublishinghouse/', views.PublishingHouseCreateView.as_view()),
    path('updatepublishinghouse/<int:pk>', views.PublishingHouseUpdateView.as_view()),
    path('deletepublishinghouse/<int:pk>', views.PublishingHouseDeleteView.as_view()),
    path('success/', views.success_page)
]
