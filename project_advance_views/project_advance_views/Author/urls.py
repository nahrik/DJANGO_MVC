from django.urls import path
from . import views 

urlpatterns = [
    path(' ',views.Author, name = 'nama_author'),
]