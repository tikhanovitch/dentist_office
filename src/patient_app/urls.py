from django.urls import path
from .views import register
from django.urls import include
from . import views


urlpatterns = [
    # path('some_url', some_view),
    path('register', register, name='register'),
    # path('register/', views.register, name='register'),

]
