# Generated by Django 3.1.2 on 2022-07-16 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('price', models.FloatField(verbose_name='Стоимость')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('release_date', models.DateField(verbose_name='Дата выхода')),
                ('lte_exists', models.BooleanField(verbose_name='Наличие lte')),
                ('slug', models.SlugField(verbose_name='URL')),
            ],
        ),
    ]