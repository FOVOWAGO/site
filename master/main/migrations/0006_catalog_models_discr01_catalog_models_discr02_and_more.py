# Generated by Django 4.2.3 on 2023-07-07 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_delete_novosti_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog_models',
            name='discr01',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='В результате обучения выпускник программы будет способен'),
        ),
        migrations.AddField(
            model_name='catalog_models',
            name='discr02',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='В результате обучения выпускник программы будет способен'),
        ),
        migrations.AddField(
            model_name='catalog_models',
            name='discr03',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='В результате обучения выпускник программы будет способен'),
        ),
        migrations.AddField(
            model_name='catalog_models',
            name='discr04',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='В результате обучения выпускник программы будет способен'),
        ),
        migrations.AddField(
            model_name='catalog_models',
            name='discr05',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='В результате обучения выпускник программы будет способен'),
        ),
        migrations.AddField(
            model_name='catalog_models',
            name='discr06',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='В результате обучения выпускник программы будет способен'),
        ),
        migrations.AddField(
            model_name='catalog_models',
            name='discr07',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='В результате обучения выпускник программы будет способен'),
        ),
        migrations.AddField(
            model_name='catalog_models',
            name='discr08',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='В результате обучения выпускник программы будет способен'),
        ),
        migrations.AddField(
            model_name='catalog_models',
            name='format',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Формат обучения'),
        ),
        migrations.AddField(
            model_name='catalog_models',
            name='obyem',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Объем программы'),
        ),
        migrations.AddField(
            model_name='catalog_models',
            name='osob',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Особенности программы'),
        ),
        migrations.AddField(
            model_name='catalog_models',
            name='zanyatia',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Количество'),
        ),
    ]
