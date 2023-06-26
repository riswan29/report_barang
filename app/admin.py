from django.contrib import admin
from .models import *


class ReportSYS(admin.ModelAdmin):
    list_display = ('id', 'n_pelapor', 'dep_pelapor','n_barang', 'keterangan', 'status')
    list_filter = ('status',)
    search_fields = ('n_barang',)
admin.site.register(Report, ReportSYS)
admin.site.register(User)
