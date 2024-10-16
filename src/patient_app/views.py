from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm, LoginForm, UserPersonalAccountForm, AppointmentForm
from .models import User


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    auth.logout(request)
    return redirect('main')


def add_personal_account(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserPersonalAccountForm(request.POST, request.FILES)
        if form.is_valid():
            personal_account = form.save(commit=False)
            personal_account.user = user
            personal_account.save()
            return redirect('personal_account', user_id=user.id)
    else:
        form = UserPersonalAccountForm(initial={'first_name': user.first_name})

    return render(request, 'add_personal_account.html', {'form': form})


def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'create_appointment.html', {'form': form})


class MainTemplateView(TemplateView):
    template_name = "main.html"


class UserPersonalAccountTemplateView(TemplateView):
    template_name = "personal_account.html"



