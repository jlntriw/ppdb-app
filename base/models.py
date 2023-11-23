from django.utils import timezone
from django.db import models
from django.core import validators
from django.db import models
import datetime

# Create your models here.



class dataSiswa(models.Model):
    nama = models.CharField(max_length=300)
    noPendaftaran = models.CharField(max_length=300, blank=True , null=True)
    nik = models.CharField(max_length=16 , validators=[validators.MinLengthValidator(limit_value=16), validators.MaxLengthValidator(limit_value=16)])
    nokk = models.CharField(max_length = 16 , blank=True, null=True, validators=[validators.MinLengthValidator(limit_value=16), validators.MaxLengthValidator(limit_value=16)])
    nisn = models.CharField(max_length=10, validators=[validators.MinLengthValidator(limit_value=10), validators.MaxLengthValidator(limit_value=10)])
    tempat_lahir = models.CharField(max_length=400, blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    asal_sekolah = models.CharField(max_length=400 , blank=True, null=True)
    asal_kabupaten = models.CharField(max_length=400 , blank=True, null=True)
    alamat = models.CharField(max_length=500, blank=True, null=True)
    jenis_kelamin = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    nomor_telepon = models.CharField(max_length=15, blank=True, null=True)
    # informasi tambahan
    namaAyah = models.CharField(max_length=400 , blank=True, null=True)
    pekerjaanAyah = models.CharField(max_length=400 , blank=True, null=True)
    nikAyah = models.IntegerField(  blank=True, null=True)
    namaIbu = models.CharField(max_length=400 , blank=True, null=True)
    nikIbu = models.IntegerField(blank=True, null=True)
    pekerjaanIbu = models.CharField(max_length=400 , blank=True, null=True)
    noKip  = models.IntegerField(  blank=True, null=True)
    noPkh  = models.IntegerField(  blank=True, null=True)
    tahun = models.IntegerField(verbose_name="Tahun", auto_created=True)
    
    def __str__(self):
        return self.nama
    


class RekapPembayaran(models.Model):
    siswa = models.ForeignKey(dataSiswa, on_delete=models.CASCADE)
    tanggal_rekap = models.DateField()
    total_pembayaran = models.DecimalField(max_digits=10, decimal_places=2)
    keterangan = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Rekap Pembayaran {self.siswa.nama} - {self.tanggal_rekap}"


class pengaturan(models.Model):
    kuota = models.IntegerField(blank=True, null=True)
    total_pembayaran = models.DecimalField(blank=True, null=True ,max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"pengaturan"
    