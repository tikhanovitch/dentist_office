from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def some_view(request):
    return HttpResponse("hello doctor app")
