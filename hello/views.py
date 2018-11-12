from django.shortcuts import render
from django.http import HttpResponse
from hello.models import User


# Create your views here.
# class User:
#     def __init__(self, name, pwd):
#         self.name = name
#         self.pwd = pwd


def index(request):
    feng = User(username='feng', age=18)
    feng.save()
    zhou = User(username='zhou', age=22)
    zhou.save()
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})
