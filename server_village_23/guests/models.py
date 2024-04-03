from django.db import models

from rooms.models import Rooms


# Create your models here.

class Guest(models.Model):
    """Гость"""

    guest_id = models.AutoField(primary_key=True, verbose_name="Id гостя")
    passport = models.CharField(max_length=255, verbose_name="Номер паспорта")
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=255, verbose_name="Отчество")
    number_room = models.ForeignKey(Rooms, on_delete=models.CASCADE, verbose_name="Номер номера")
    check_in_date = models.DateField(verbose_name="Дата заезда")
    check_out_date = models.DateField(verbose_name="Дата выезда")

    def __str__(self):
        return f"{self.guest_id}"

    class Meta:
        verbose_name = "Гость"
        verbose_name_plural = "Гости"


class GuestServices(models.Model):
    """Услуги для гостя в номер"""

    service_id = models.AutoField(primary_key=True, verbose_name="Id")
    guest_id_service = models.ForeignKey(Guest, on_delete=models.CASCADE, verbose_name="Id гостя")
    service_name = models.CharField(max_length=255, verbose_name="Услуга")

    class Meta:
        verbose_name = "Услуга в номер"
        verbose_name_plural = "Услуги в номер"
