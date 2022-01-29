from django.db import models
from django.utils.translation import gettext as _


class Publication(models.Model):
    """Model publication"""
    date = models.DateField(
        verbose_name=_("Дата публикации"),
    )
    subject = models.CharField(
        verbose_name=_("Заголовок новости"),
        max_length=256,
    )
    content = models.TextField(
        verbose_name=_("Содержание новости"),
    )

    class Meta:
        verbose_name = _("Publication")
        verbose_name_plural = _("Publications")
        ordering = ('-date', )

    def __str__(self):
        return self.subject
