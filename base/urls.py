from django.urls import path
from .views import detail_siswa,export_rekap_pembayaran_to_excel ,  daftar_siswa, input_rekap_pembayaran, pendaftaran_siswa, rekap_pembayaran, user_login, user_logout, edit_siswa, delete_siswa, export_to_excel
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', daftar_siswa, name='daftar-siswa'),
    path('pendaftaran/', login_required(pendaftaran_siswa), name='pendaftaran'),
    path('login/', user_login, name='user-login'),
    path('logout/', user_logout, name='user-logout'),
    path('siswa/edit/<int:pk>', edit_siswa, name='edit-siswa'),
    path('delete-siswa/<int:pk>', delete_siswa, name='delete-siswa'),
    path('export-excel/', export_to_excel , name='export-excel'),
    path('siswa/<int:pk>/input-rekap-pembayaran/', input_rekap_pembayaran, name='input-rekap-pembayaran'),
    path('siswa/<int:pk>/', detail_siswa, name='detail-siswa'),
    path('rekap-pembayaran/', rekap_pembayaran, name='rekap-pembayaran'),
    path('export_rekap_pembayaran_to_excel/', export_rekap_pembayaran_to_excel, name='export_rekap_pembayaran_to_excel'),

     
   

    
]