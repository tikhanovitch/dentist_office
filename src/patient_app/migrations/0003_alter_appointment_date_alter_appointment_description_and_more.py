# Generated by Django 5.0.4 on 2024-10-16 15:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_app', '0002_userpersonalaccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='description',
            field=models.TextField(verbose_name='Описание проблемы'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='userpersonalaccount',
            name='phone_number',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message="Номер телефона должен быть в формате '+375XX XXXXXXX'.", regex='^\\+375\\d{2}\\d{7}$')]),
        ),
    ]
