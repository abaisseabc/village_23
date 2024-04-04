from django.db import models


# Create your models here.

class CallRequests(models.Model):
    """Заявки на звонок"""

    call_id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=255, verbose_name="Телефон")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата оформления заявки на звонок")

    class Meta:
        ordering = ("-date_added",)
        verbose_name = "Заявка на звонок"
        verbose_name_plural = "Заявки на звонок"
