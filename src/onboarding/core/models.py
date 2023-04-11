from django.db import models


class OfficeMap(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название")
    photo = models.ImageField(upload_to="images/", verbose_name="Фото")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "План офиса"
        verbose_name_plural = "Планы офиса"
        ordering = ["id", "title"]
