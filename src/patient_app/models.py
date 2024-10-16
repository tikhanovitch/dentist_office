# Create your models here.

from django.db import models
from django.core.validators import RegexValidator


class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)


class Appointment(models.Model):  # запись на прием. Создать поле Ф.И.О.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(verbose_name="Дата")
    time = models.TimeField(verbose_name="Время")
    description = models.TextField(verbose_name="Описание проблемы")


class UserPersonalAccount(models.Model):  # личный кабинет
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=30, null=True)
    phone_number = models.CharField(
        max_length=12,
        validators=[RegexValidator(
            regex=r'^\+375\d{2}\d{7}$',
            message="Номер телефона должен быть в формате '+375XX XXXXXXX'."
        )]
    )
    photo = models.ImageField(null=True, blank=True, upload_to="user_photo/")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


