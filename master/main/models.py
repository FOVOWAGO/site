from django.db import models


class Post_models(models.Model):
    name = models.CharField('Имя', max_length=100)
    surname = models.CharField('Фамилия', max_length=100)
    father_name = models.CharField('Отчество', max_length=100)
    num = models.CharField('Номер телефона', max_length=20)
    email = models.EmailField('Email')
    roj = models.DateField('Дата рождения', max_length=100)
    graj = models.CharField('Гражданство', max_length=100)
    region = models.CharField('Регион', max_length=100)
    programm = models.CharField('Программа', max_length=100)
    category = models.CharField('Категория участника', max_length=100)
    zan = models.CharField('Текущая занятость', max_length=100)
    reg_bezrab = models.CharField('Срок регистрации безработным', max_length=100)
    obraz = models.CharField('Ваше текущее образование', max_length=100)
    galka = models.BooleanField('Ответили', default=False)
    vremya = models.DateTimeField('Дата отправки', auto_now_add=True)


    class Meta:
        verbose_name = "Заявки"
        verbose_name_plural = "Заявки"

class Catalog_models(models.Model):
    image_main = models.ImageField('Фото(основное)', blank=True, null=True)
    image_sec = models.ImageField('Фото', blank=True, null=True)
    image3 = models.ImageField('Фото(доп)', blank=True, null=True)
    image4 = models.ImageField('Фото(доп)', blank=True, null=True)
    name = models.CharField('Название новости', max_length=100, blank=True, null=True)
    announce = models.CharField('Анонс', max_length=1000, blank=True, null=True)
    discr1 = models.CharField('Описание', max_length=100, blank=True, null=True)
    discr2 = models.CharField('Описание', max_length=100, blank=True, null=True)
    discr3 = models.CharField('Описание', max_length=100, blank=True, null=True)
    discr4 = models.CharField('Описание', max_length=100, blank=True, null=True)
    discr5 = models.CharField('Описание', max_length=100, blank=True, null=True)
    date = models.DateField('Дата добавления', auto_now_add=True, blank=True, null=True)
    osob = models.CharField('Особенности программы', max_length=1000, blank=True, null=True)
    ysl = models.TextField('Условия и режим реализации', blank=True, null=True)
    obyem = models.CharField('Объем программы', max_length=1000, blank=True, null=True)
    format = models.CharField('Формат обучения', max_length=1000, blank=True, null=True)
    zanyatia = models.CharField('Количество занятий', max_length=1000, blank=True, null=True)
    discr01 = models.CharField('В результате обучения выпускник программы будет способен', max_length=1000, blank=True, null=True)
    discr02 = models.CharField('В результате обучения выпускник программы будет способен', max_length=1000, blank=True, null=True)
    discr03 = models.CharField('В результате обучения выпускник программы будет способен', max_length=1000, blank=True, null=True)
    discr04 = models.CharField('В результате обучения выпускник программы будет способен', max_length=1000, blank=True, null=True)
    discr05 = models.CharField('В результате обучения выпускник программы будет способен', max_length=1000, blank=True, null=True)
    discr06 = models.CharField('В результате обучения выпускник программы будет способен', max_length=1000, blank=True, null=True)
    discr07 = models.CharField('В результате обучения выпускник программы будет способен', max_length=1000, blank=True, null=True)
    discr08 = models.CharField('В результате обучения выпускник программы будет способен', max_length=1000, blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Каталог программ"
        verbose_name_plural = "Каталог программ"