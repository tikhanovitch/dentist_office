from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('main/', views.MainTemplateView.as_view(), name='main'),
    path('personal_account/', views.UserPersonalAccountTemplateView.as_view(), name='personal_account'),
    path('add_personal_account/', views.add_personal_account, name='add_personal_account'), #<int:user_id>/

]
