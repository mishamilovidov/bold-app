from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from project3.models import User, Equipment, Department, Manufacturer
# from project3.forms import UserForm, EquipmentForm, DepartmentForm, ManufacturerForm

from django.contrib import messages


def login_view(request):
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'Please contact your administrator to activate your account.')
        else:
            messages.error(request, 'Login is invalid.')
    context_dict = {'request': request}
    return render(request, 'login.html', context_dict)


def logout_user(request):
    logout(request)
    return render(request, "login.html")


@login_required(login_url='/login/')
def index(request):
    context_dict = {'request': request}
    return render(request, "home.html", context_dict)


@login_required(login_url='/login/')
def tableau(request):
    context_dict = {'request': request}
    return render(request, "tableau.html", context_dict)

@login_required(login_url='/login/')
def prediction(request):
    context_dict = {'request': request}
    return render(request, "prediction.html", context_dict)

