from django.urls import path
from . import views

urlpatterns = [
    path('admin/imdbapi/', views.imdb_api_admin, name='imdb_api_admin'),
    path('user/imdbapi/', views.imdb_api_user, name='imdb_api_user')
]
