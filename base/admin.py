from django.contrib import admin
from .models import dataSiswa, RekapPembayaran, pengaturan
# Register your models here.
admin.site.register(dataSiswa)
admin.site.register(RekapPembayaran)
admin.site.register(pengaturan)
# admin.site.site_header = "Admin PPDB"