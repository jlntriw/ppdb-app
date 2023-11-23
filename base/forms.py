from django import forms
from .models import dataSiswa

from .models import RekapPembayaran



class PendaftaranSiswaForm(forms.ModelForm):
    class Meta:
        model = dataSiswa
        exclude = ['tahun']

    


class RekapPembayaranForm(forms.ModelForm):
    class Meta:
        model = RekapPembayaran
        fields = ['tanggal_rekap', 'total_pembayaran', 'keterangan']

