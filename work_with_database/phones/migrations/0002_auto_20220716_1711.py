# Generated by Django 3.1.2 on 2022-07-16 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.URLField(default=None, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(default=None, verbose_name='Наличие lte'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.IntegerField(default=None, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.DateField(default=None, verbose_name='Дата выхода'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default=None, max_length=255, verbose_name='URL'),
        ),
    ]
