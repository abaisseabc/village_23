from django.db import models


# Create your models here.

class TypeRooms(models.Model):
    """Типы номеров"""

    type_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100, verbose_name="Тип номера на английском")
    type_rus = models.CharField(max_length=100, verbose_name="Тип номера на русском")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Тип номера"
        verbose_name_plural = "Типы номеров"


class Rooms(models.Model):
    """Номера"""

    room_id = models.AutoField(primary_key=True)
    room_type = models.ForeignKey(TypeRooms, on_delete=models.CASCADE, verbose_name="Тип номера")
    room_number = models.IntegerField(verbose_name="Номер номера")
    view_window = models.CharField(max_length=100, verbose_name="Вид из окна")
    size = models.IntegerField(verbose_name="Размер комнаты в м2")
    type_bed = models.CharField(max_length=100, verbose_name="Размер кровати")
    price = models.IntegerField(verbose_name="Цена")
    image = models.ImageField(upload_to="rooms/", blank=True, null=True, verbose_name="Фотография")

    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Номера"

    def __str__(self):
        return str(self.room_number)

    def get_image(self):
        if self.image:
            return "http://127.0.0.1:8000" + self.image.url
        return ""
