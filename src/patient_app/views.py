from django.http import HttpResponse


from django.shortcuts import render, redirect
from .models import User
# from .forms import UserRegistrationForm


def register_view(request):  # регистрация пользователя и редирект на 'login' для входа
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    # TO DO: реализация функции входа
    pass
