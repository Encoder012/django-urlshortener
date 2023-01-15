from asyncio.windows_events import INFINITE
from tabnanny import verbose
from django.db import models

# Create your models here.
class URLS(models.Model):
    longUrl = models.CharField(max_length=INFINITE)
    shortUrl = models.CharField(max_length=INFINITE)
    urlCode = models.CharField(max_length=INFINITE, default=None)
    multipleCode = models.TextField(max_length=INFINITE, default="[]")
    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URLS'