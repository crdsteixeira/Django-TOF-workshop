from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Book(models.Model):

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Book')
    
    name = models.CharField(_('Name'), max_length = 100)
    author = models.CharField(_('Author'), max_length=100)
    description = models.TextField(_('Description'))


