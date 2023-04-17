from django.db import models


class Users(models.Model):
    external_id = models.PositiveBigIntegerField(verbose_name="ID пользователя")
    name = models.CharField(verbose_name="Имя")

    def __str__(self):
        return f"{self.name}" if self.name else f"{self.external_id}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
