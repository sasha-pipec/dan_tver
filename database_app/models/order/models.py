from django.db import models


class Order(models.Model):
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    age = models.IntegerField(verbose_name='Возраст')
    experience = models.TextField(verbose_name='Наличие опыта или лицензии')
    phone_number = models.CharField(max_length=20, verbose_name='Номера телефона')
    is_agreed = models.BooleanField(default=False, verbose_name='Согласие на обработку перс. данных')
    is_checked = models.BooleanField(default=False, verbose_name='Заявка просмотрена')

    def __str__(self):
        return f'{self.fio} - {self.phone_number}'

    class Meta:
        db_table = 'orders'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
