from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class Report(models.Model):
    # membuat opsi untuk status
    STATUS_CHOICES = (
        ('belum', 'Belum Diproses'),
        ('sedang', 'Sedang Diproses'),
        ('selesai', 'Selesai Diproses'),
    )
    id = models.AutoField(primary_key=True)
    n_pelapor = models.CharField(max_length=100)
    j_pelapor = models.CharField(max_length=100)
    dep_pelapor = models.CharField(max_length=100)
    n_barang = models.CharField(max_length=100)
    keterangan = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    keterangan_petugas = models.TextField()
    tgl_lapor = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"KD{self.id:03}"
    class Meta:
        ordering = ['id']
    def save(self, *args, **kwargs):
        if not self.id:
            last_report = Report.objects.order_by('id').first()
            if last_report:
                last_id = last_report.id
                self.id = last_id + 1
            else:
                self.id = 1
        super().save(*args, **kwargs)

class User(AbstractUser):
    LEVEL_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='user_images/')
    status = models.CharField(max_length=100, choices=LEVEL_CHOICES)
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user'
    )

    def __str__(self):
        return self.username
