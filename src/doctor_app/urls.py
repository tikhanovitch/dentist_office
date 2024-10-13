from django.urls import path
from .views import some_view
from django.urls import include
from . import views


urlpatterns = [
    path('some_url', some_view),
]
