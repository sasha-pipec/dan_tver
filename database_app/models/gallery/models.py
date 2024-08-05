from django.db import models


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/', verbose_name='Картинки галереи')

    def __str__(self):
        return self.image.url

    class Meta:
        db_table = 'galleries'
        verbose_name = 'Картинки галереи'
        verbose_name_plural = 'Картинки галереи'
