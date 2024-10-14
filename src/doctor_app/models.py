from django.core.validators import RegexValidator
from django.db import models

# Create your models here.


class PatientCardMainPart(models.Model):  # стоматологическая амбулаторная карта
    SEX_PATIENT = {
        "м": "мужской",
        "ж": "женский",
    }
    surname = models.CharField(max_length=50, null=False, verbose_name="Фамилия")
    name = models.CharField(max_length=50, null=False, verbose_name="Имя")
    patronymic = models.CharField(max_length=50, null=False, verbose_name="Отчество")
    birth_date = models.DateField(verbose_name="Число, месяц, год рождения")
    sex = models.CharField(max_length=1, choices=SEX_PATIENT, null=False, verbose_name="Пол")
    address = models.CharField(max_length=50, null=False, verbose_name="Адрес постоянной (временной) регистрации")
    phone_number = models.CharField(
        max_length=13,
        validators=[RegexValidator(
            regex=r'^\+375\d{2}\d{7}$',
            message="Phone number must be entered in the format '+375XX XXX XX XX'."
        )],
        verbose_name="Номер контактного телефона"
    )
    social_status = models.CharField(max_length=100, null=True, verbose_name="Социальное положение")
    place_of_work = models.CharField(max_length=100, null=True, verbose_name="Место работы (службы, учебы)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заполнения")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"


class PatientCardXRayPart(models.Model):  # лист назначений и учета нагрузок
    type_of_research = models.CharField(  # рентгенологических исследований
        max_length=50,
        null=False,
        verbose_name="Назначен вид исследования"
    )
    PRESCRIBED = {
        "КОП": "К.О.П.",
        "ИИИ": "И.И.И.",
    }
    prescribed_doctor = models.CharField(
        max_length=50,
        choices=PRESCRIBED,
        null=False,
        verbose_name="Назначил (врач)"
    )
    research_conducted = models.CharField(
        max_length=50,
        null=False,
        verbose_name="Проведено исследование (организация)"
    )
    event_date = models.DateField(verbose_name="Дата проведения")
    equivalent_dose = models.FloatField(null=False, verbose_name="Эквивалентная доза(мЗВ)")
    patient = models.ForeignKey(PatientCardMainPart, on_delete=models.CASCADE, related_name='xray_appointments')
