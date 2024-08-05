from django.db import models


class Award(models.Model):
    image = models.ImageField(upload_to='awards/', verbose_name='Картинки наград')

    def __str__(self):
        return self.image.url

    class Meta:
        db_table = 'awards'
        verbose_name = 'Картинки наград'
        verbose_name_plural = 'Картинки наград'
