from django.contrib import admin
from .models import (
    PatientCardMainPart,
    PatientCardXRayPart,
    VisitsDiary,
)

#  _____Inlines_____


class PatientCardXRayPartInline(admin.TabularInline):
    model = PatientCardXRayPart
    extra = 1


class VisitsDiaryInLine(admin.TabularInline):
    model = VisitsDiary
    extra = 1

#  _____End Inlines_____

#  _____Admins_____


class PatientCardMainPartAdmin(admin.ModelAdmin):
    list_display = [
        "surname", "name", "patronymic",
        "birth_date", "sex", "address",
        "phone_number", "social_status",
        "place_of_work", "created_at",
    ]
    inlines = [
        PatientCardXRayPartInline,
        VisitsDiaryInLine,
    ]
    search_fields = ["surname", "name", "patronymic"]

#  _____End Admins_____


admin.site.register(PatientCardMainPart, PatientCardMainPartAdmin)
# admin.site.register(PatientCardMainPart)
admin.site.register(PatientCardXRayPart)
admin.site.register(VisitsDiary)
