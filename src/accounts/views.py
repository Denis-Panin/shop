from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User

def users(request):
    # template = loader.get_template('accounts/index.html')
    # return HttpResponse('Hello world')
    return render(request, 'accounts/index.html')
