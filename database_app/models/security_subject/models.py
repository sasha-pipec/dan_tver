from django.db import models


class SecuritySubject(models.Model):
    text = models.TextField(verbose_name='Охроняемые объекты.')

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'security_subjects'
        verbose_name = 'Охроняемый объект'
        verbose_name_plural = 'Охроняемые объекты'
