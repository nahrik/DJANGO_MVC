from django.db.models import TextField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.utils import timezone

from django.db import models as models

# Create your models here.
class Hewan(models.Model): 
    nama = models.TextField(max_length=255)
    species = models.TextField(max_length=255)
    berat = models.TextField(max_length=3)
    umur = models.CharField(max_length=3)

    def __str__(self): 
        return self.nama

class Kandang(models.Model): 
    nama = models.TextField(max_length=255)
    isi_kandang = models.TextField(max_length=255)
    luas_kandang = models.CharField(max_length=5)
    
    def __str__(self): 
        return self.nama

class Penjaga(models.Model): 
    nama = models.TextField(max_length=255)
    nomor_telepon = models.TextField(max_length=25)
    jadwal_jaga = models.DateTimeField(default=timezone.now)

    def __str__(self): 
        return self.nama

class Pengunjung(models.Model): 
    nama = models.TextField(max_length=255)
    nomor_telepon = models.TextField(max_length=25)
    hari_berkunjung = models.TextField(max_length=15)

    def __str__(self): 
        return self.nama
