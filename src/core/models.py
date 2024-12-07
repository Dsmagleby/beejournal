from django.conf import settings
from django.db import models
from simple_history.models import HistoricalRecords


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(app_label)s_%(class)s_related",
        on_delete=models.PROTECT,
        null=True, blank=True
    )
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
    
    @property
    def class_name(self):
        return self.__class__.__name__
