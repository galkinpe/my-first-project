from django.conf import settings
from django.db import models
from django.utils import timezone


class Record(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Наименование')
    text = models.TextField(verbose_name='Текст')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Создан')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Размещен')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован?')




    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-created_date']