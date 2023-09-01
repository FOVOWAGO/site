from django.db import models

class Novosti_models(models.Model):
    image = models.ImageField('Фото')
    name = models.CharField('Название новости', max_length=150)
    announce = models.CharField('Анонс', max_length=1000)
    date = models.DateField('Дата публикации', auto_now_add=True)
    full = models.TextField('Вся новость', blank=True, null=True)
    source = models.CharField('Источник:', max_length=100, blank=True, null=True)


    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"