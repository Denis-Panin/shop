from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def users(request):
    return HttpResponse('hello Users')
