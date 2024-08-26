from django.contrib import admin

from database_app.models import SecuritySubject


@admin.register(SecuritySubject)
class SecuritySubjectAdmin(admin.ModelAdmin):
    pass
