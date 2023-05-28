from django.db import models
from django.urls import reverse


# Create your models here.
class PictureHome(models.Model):
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/",blank=True,verbose_name='Фото на заставочном экране')

    class Meta:#для вида в админки
        verbose_name = 'Фото на заставочном экране'
        verbose_name_plural = 'Фото на заставочном экране'
        ordering = ['photo',]

