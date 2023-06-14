from django.urls import path
from reference import views

app_name = 'reference'
urlpatterns = [
    path('allgenres/', views.GenreListView.as_view(), name='list-genre'),
    path('creategenre/', views.GenreCreateView.as_view(), name='create-genre'),
    path('updategenre/<int:pk>', views.GenreUpdateView.as_view(), name='update-genre'),
    path('deletegenre/<int:pk>', views.GenreDeleteView.as_view(), name='delete-genre'),
    path('productdetails/<int:pk>', views.TitleDetailView.as_view(), name='detail-title'),
    path('alltitles/', views.TitleListView.as_view(), name='list-title'),
    path('createtitle/', views.TitleCreateView.as_view(), name='create-title'),
    path('updatetitle/<int:pk>', views.TitleUpdateView.as_view(), name='update-title'),
    path('deletetitle/<int:pk>', views.TitleDeleteView.as_view(), name='delete-title'),
    path('allauthors/', views.AuthorListView.as_view(), name='list-author'),
    path('createauthor/', views.AuthorCreateView.as_view(), name='create-author'),
    path('updateauthor/<int:pk>', views.AuthorUpdateView.as_view(), name='update-author'),
    path('deleteauthor/<int:pk>', views.AuthorDeleteView.as_view(), name='delete-author'),
    path('alleditions/', views.EditionListView.as_view(), name='list-edition'),
    path('createedition/', views.EditionCreateView.as_view(), name='create-edition'),
    path('updateedition/<int:pk>', views.EditionUpdateView.as_view(), name='update-edition'),
    path('deleteedition/<int:pk>', views.EditionDeleteView.as_view(), name='delete-edition'),
    path('allpublishinghouses/', views.PublishingHouseListView.as_view(), name='list-publishing-house'),
    path('createpublishinghouse/', views.PublishingHouseCreateView.as_view(), name='create-publishing-house'),
    path('updatepublishinghouse/<int:pk>', views.PublishingHouseUpdateView.as_view(), name='update-publishing-house'),
    path('deletepublishinghouse/<int:pk>', views.PublishingHouseDeleteView.as_view(), name='delete-publishing-house')
]