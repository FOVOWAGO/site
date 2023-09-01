# Generated by Django 4.2.3 on 2023-07-07 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_catalog_models_discr01_catalog_models_discr02_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog_models',
            name='ysl',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Условия и режим реализации'),
        ),
        migrations.AlterField(
            model_name='catalog_models',
            name='announce',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Анонс'),
        ),
        migrations.AlterField(
            model_name='catalog_models',
            name='date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='catalog_models',
            name='discr1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='catalog_models',
            name='discr2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='catalog_models',
            name='discr3',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='catalog_models',
            name='discr4',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='catalog_models',
            name='discr5',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='catalog_models',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото(доп)'),
        ),
        migrations.AlterField(
            model_name='catalog_models',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото(доп)'),
        ),
        migrations.AlterField(
            model_name='catalog_models',
            name='image_main',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото(основное)'),
        ),
        migrations.AlterField(
            model_name='catalog_models',
            name='image_sec',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='catalog_models',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название новости'),
        ),
    ]