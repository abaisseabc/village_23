from django.db import models


# Create your models here.

class Bookings(models.Model):
    """Бронь"""

    booking_id = models.AutoField(primary_key=True)
    check_in_date = models.DateField(verbose_name="Дата заезда")
    check_out_date = models.DateField(verbose_name="Дата выезда")
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    phone = models.CharField(max_length=255, verbose_name="Телефон")
    STATUS_CHOICES = [
        ("confirmed", "Подтверждено"),
        ("pending", "Ожидает подтверждения"),
        ("cancelled", "Отменено"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name="Статус")

    def __str__(self):
        return f"Бронь от {self.first_name} с датой заезда {self.check_in_date}"

    class Meta:
        ordering = ("check_in_date",)
        verbose_name = "Бронь"
        verbose_name_plural = "Брони"
