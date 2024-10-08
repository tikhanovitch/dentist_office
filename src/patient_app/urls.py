from django.urls import path
from .views import register
from django.urls import include


urlpatterns = [
    # path('some_url', some_view),
    path('register', register, name='register'),


]
