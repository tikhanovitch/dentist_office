from django.urls import path
from .views import some_view

urlpatterns = [
    path('some_url', some_view),

]
