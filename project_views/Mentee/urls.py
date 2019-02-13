from django.urls import path
from . import views 

urlpatterns = [
    path(' ',views.Mentee, name = 'nama_mentee'),
]