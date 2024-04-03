from django.db import models


# Create your models here.

class News(models.Model):
    """Новости"""

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(verbose_name="Имя заголовка на английском")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to="news/", blank=True, null=True, verbose_name="Фотография")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        ordering = ("-date_added",)
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return "http://127.0.0.1:8000" + self.image.url
        return ""
