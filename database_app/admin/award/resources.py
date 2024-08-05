from django.contrib import admin
from django.utils.safestring import mark_safe

from database_app.models import Award


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_html_photo',)

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(
                "<div style='width:100px; background:white;'>"
                f"<a href='{object.image.url}'>"
                f"<img src='{object.image.url}' width=100>"
                "</a>"
                "</div>"
            )

    get_html_photo.short_description = 'Картинки наград'
