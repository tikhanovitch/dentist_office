from django.contrib import admin

# Register your models here.


from .models import (
    PatientCardMainPart,
    PatientCardXRayPart,
    VisitsDiary,
)


admin.site.register(PatientCardMainPart)
admin.site.register(PatientCardXRayPart)
admin.site.register(VisitsDiary)
