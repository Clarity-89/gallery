from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_added', 'location', 'picture']
    list_filter = ['date_added', 'location']
    search_fields = ['title', 'date_added', 'location', 'picture']
