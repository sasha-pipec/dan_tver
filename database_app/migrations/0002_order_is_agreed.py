# Generated by Django 4.0 on 2024-08-04 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_agreed',
            field=models.BooleanField(default=False, verbose_name='Согласие на обработку перс. данных '),
        ),
    ]
