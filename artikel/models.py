from django.db import models
from django.utils.text import slugify


class Artikel(models.Model):
    judul = models.CharField(max_length=255, null=True, blank=True)
    isi = models.TextField(null=True, blank=True)
    kategori = models.CharField(max_length=255, null=True, blank=True)
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True, editable=False)

    def save(self):
        self.slug = slugify(self.judul)
        super().save()

    def __str__(self):
        return f"{self.id} - {self.judul}"
