from django.contrib import admin

from database_app.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('fio', 'age', 'experience', 'phone_number', 'is_checked')
    list_editable = ('is_checked',)
    list_filter = ('is_checked',)
