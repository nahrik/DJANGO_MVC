from django.contrib import admin
from .models import Dokter, Pasien, Resep, Obat
# Register your models here.

my_model = [Dokter, Pasien, Resep, Obat]
admin.site.register(my_model)