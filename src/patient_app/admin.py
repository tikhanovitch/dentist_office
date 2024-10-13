from django.contrib import admin

# Register your models here.
from .models import (
    User,
    Appointment,
    UserPersonalAccount,
)


admin.site.register(User)
admin.site.register(Appointment)
admin.site.register(UserPersonalAccount)
