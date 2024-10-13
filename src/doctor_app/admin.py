from django.contrib import admin

# Register your models here.


from .models import (
    PatientCardMainPart,
)


admin.site.register(PatientCardMainPart)
