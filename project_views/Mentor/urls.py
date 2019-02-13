from django.urls import path
from . import views 

urlpatterns = [
    path(' ',views.Mentor, name = 'nama_mentor'),
]