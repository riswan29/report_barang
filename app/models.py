from django.db import models

class Report(models.Model):
    # membuat opsi untuk status
    STATUS_CHOICES = (
        ('belum', 'Belum Diproses'),
        ('sedang', 'Sedang Diproses'),
        ('selesai', 'Selesai Diproses'),
    )

    n_pelapor = models.CharField(max_length=100)
    j_pelapor = models.CharField(max_length=100)
    dep_pelapor = models.CharField(max_length=100)
    n_barang = models.CharField(max_length=100)
    keterangan = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    keterangan_petugas = models.TextField()
    tgl_lapor = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.n_pelapor
