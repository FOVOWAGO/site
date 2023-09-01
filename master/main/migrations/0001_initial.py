# Generated by Django 4.2.2 on 2023-07-03 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog_models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_main', models.ImageField(upload_to='', verbose_name='Фото(основное)')),
                ('image_sec', models.ImageField(upload_to='', verbose_name='Фото')),
                ('image3', models.ImageField(upload_to='', verbose_name='Фото(доп)')),
                ('image4', models.ImageField(upload_to='', verbose_name='Фото(доп)')),
                ('name', models.CharField(max_length=100, verbose_name='Название новости')),
                ('announce', models.CharField(max_length=100, verbose_name='Анонс')),
                ('discr1', models.CharField(max_length=100, verbose_name='Описание')),
                ('discr2', models.CharField(max_length=100, verbose_name='Описание')),
                ('discr3', models.CharField(max_length=100, verbose_name='Описание')),
                ('discr4', models.CharField(max_length=100, verbose_name='Описание')),
                ('discr5', models.CharField(max_length=100, verbose_name='Описание')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата добавления')),
            ],
        ),
        migrations.CreateModel(
            name='Novosti_models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('name', models.CharField(max_length=100, verbose_name='Название новости')),
                ('announce', models.CharField(max_length=100, verbose_name='Анонс')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
                ('full', models.TextField(blank=True, null=True, verbose_name='Вся новость')),
                ('source', models.CharField(blank=True, max_length=100, null=True, verbose_name='Источник:')),
            ],
        ),
        migrations.CreateModel(
            name='Post_models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('father_name', models.CharField(max_length=100, verbose_name='Отчество')),
                ('num', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('roj', models.DateField(max_length=100, verbose_name='Дата рождения')),
                ('graj', models.CharField(max_length=100, verbose_name='Гражданство')),
                ('region', models.CharField(max_length=100, verbose_name='Регион')),
                ('programm', models.CharField(max_length=100, verbose_name='Программа')),
                ('category', models.CharField(max_length=100, verbose_name='Категория участника')),
                ('zan', models.CharField(max_length=100, verbose_name='Текущая занятость')),
                ('reg_bezrab', models.CharField(max_length=100, verbose_name='Срок регистрации безработным')),
                ('obraz', models.CharField(max_length=100, verbose_name='Ваше текущее образование')),
                ('galka', models.BooleanField(default=False, verbose_name='Ответили')),
                ('vremya', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')),
            ],
        ),
    ]