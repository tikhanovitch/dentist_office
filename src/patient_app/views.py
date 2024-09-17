from django.http import HttpResponse


def some_view(request):
    return HttpResponse("test message")

#
# from django.shortcuts import render, redirect
# from .models import User
# from .forms import UserRegistrationForm
#
#
# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'register.html', {'form': form})
#
#
# def login(request):
#     # TO DO: реализация функции входа
#     pass
