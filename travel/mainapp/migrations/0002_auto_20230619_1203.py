# Generated by Django 3.2 on 2023-06-19 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.CharField(max_length=300, verbose_name='Описание новости'),
        ),
        migrations.AlterField(
            model_name='news',
            name='detailed_desc',
            field=models.CharField(default=0, max_length=10000, verbose_name='Подробное описание'),
        ),
    ]
