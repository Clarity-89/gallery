from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Photo(models.Model):
    title = models.CharField(_('title'), max_length=255)
    location = models.CharField(_('location'), max_length=255)
    date_added = models.DateField(_("date"), default=datetime.today, null=True, blank=True)
    picture = models.ImageField(_('picture'), upload_to='images', blank=True)
    description = models.TextField(_('description'), blank=True)
