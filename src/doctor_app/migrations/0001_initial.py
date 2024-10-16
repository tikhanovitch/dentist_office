# Generated by Django 5.0.4 on 2024-10-13 18:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientCardMainPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('patronymic', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('sex', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=1)),
                ('address', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format '+375XX XXXXXXX'.", regex='^\\+375\\d{2}\\d{7}$')])),
                ('social_status', models.CharField(max_length=100, null=True)),
                ('place_of_work', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
