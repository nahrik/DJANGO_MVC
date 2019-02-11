from django.db.models import CharField
from django.db.models import TextField
from django.db.models import DateTimeField
from django.utils import timezone

from django.db import models as models

# Create your models here.
class Direksi(models.Model): 
    nama_lengkap = models.TextField(max_length=255)
    nomor_telepon = models.TextField(max_length=25)
    jabatan = models.TextField(max_length=255)

    def __str__(self): 
        return self.nama_lengkap
 
class Mentee(models.Model): 
    nama_lengkap = models.TextField(max_length=255)
    nomor_telepon = models.TextField(max_length=25)
    nomor_absen = models.CharField(max_length=10)
    nilai_rata_rata = models.CharField(max_length=10)

    def __str__(self): 
        return self.nama_lengkap

class Mata_Pelajaran(models.Model): 
    nama_pelajaran = models.TextField(max_length=255)
    jadwal_dimulai = models.DateTimeField(default=timezone.now)
    jadwal_berakhir = models.DateTimeField(default=timezone.now)

    def __str__(self): 
        return self.nama_pelajaran

class Mentor(models.Model): 
    nama_lengkap = models.TextField(max_length=255)
    nomor_telepon = models.TextField(max_length=25)
    mata_pelajaran = models.ForeignKey(Mata_Pelajaran, on_delete=models.CASCADE)

    def __str__(self): 
        return self.nama_lengkap

class Challenge(models.Model): 
    nama_challenge = models.TextField(max_length=255)
    banyak_soal = models.TextField(max_length=25)
    bobot_nilai = models.CharField(max_length=3)
    mata_pelajaran = models.ForeignKey(Mata_Pelajaran, on_delete=models.CASCADE)

    def __str__(self): 
        return self.nama_challenge

class Live_Code(models.Model): 
    nama_live_code = models.TextField(max_length=255)
    banyak_soal = models.CharField(max_length=3)
    bobot_nilai = models.CharField(max_length=3)
    mata_pelajaran = models.ForeignKey(Mata_Pelajaran, on_delete=models.CASCADE)

    def __str__(self): 
        return self.nama_live_code
