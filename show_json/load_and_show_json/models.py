from django.db import models


class Module(models.Model):
    module = models.CharField(max_length=30, verbose_name="Имя модели")
    function = models.CharField(max_length=30, verbose_name="Функция")

    def __str__(self):
        return f"{self.module}/{self.function}"


class FullModuleInfo(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name="Модуль", related_name="full")
    description = models.CharField(max_length=30, verbose_name="Описание")
    version = models.CharField(max_length=100, verbose_name="Версия")
    value = models.CharField(max_length=1000, verbose_name="Массив")

    def __str__(self):
        return f"{self.module}/{self.description}"
