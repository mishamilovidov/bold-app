from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from boldapp.models import User, Equipment, Department, Manufacturer
from boldapp.forms import UserForm, EquipmentForm, DepartmentForm, ManufacturerForm

from django.contrib import messages

#login view - processes the request for a login and grants access to an authenticated user
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

# logs out a specified user
def logout_user(request):
    logout(request)
    return render(request, "login.html")

# handles request to go into the homepage of the project
@login_required(login_url='/login/')
def index(request):
    context_dict = {'request': request}
    return render(request, "home.html", context_dict)

# pulls all equipment within the database and sends it to the view to be displayed
@login_required(login_url='/login/')
def equipment(request):
    equipment = Equipment.objects.all()
    context_dict = {'request': request, 'equipment': equipment}
    return render(request, "equipments.html", context_dict)

# function that handles CRUD for all equipment -
@login_required(login_url='/login/')
def equipment_unit(request, equipmentid=None):
    try:
        # filters the request to determine if post / get
        if request.POST:
            try:
                # if an equipment id is present - then update an existing item with post data
                if equipmentid:
                    try:
                        e = Equipment.objects.get(id=equipmentid)
                        updateequipment = EquipmentForm(request.POST, instance=e)
                        updateequipment.save()
                        messages.success(request, 'Equipment Updated Successfully')
                    except Exception as e:
                        messages.success(request, 'Error Updating Equipment')
                        return HttpResponseRedirect('/equipment/')
                # if no id is present - create a new item with post data
                else:
                    newequipment = EquipmentForm(request.POST)
                    e = newequipment.save(commit=False)
                    e.save()
                    messages.success(request, 'Equipment Added Successfully')
            except Exception as e:
                messages.error(request, 'Error Adding Equipment.')
            return HttpResponseRedirect('/equipment/')
        else:
            # if id is present - view an existing item with form to edit
            if equipmentid:
                try:
                    e = Equipment.objects.get(id=equipmentid)
                    form = EquipmentForm(instance=e)
                    context_dict = {'equipment': e, 'form': form}
                    return render(request, "equipment.html", context_dict)
                except User.DoesNotExist:
                    messages.error(request, 'Equipment Does Not Exist.')
                    return HttpResponseRedirect('/equipment/')
            # if no id - create form to create new item
            else:
                form = EquipmentForm()
                context_dict = {'form': form}
                return render(request, "equipment.html", context_dict)
    except Equipment.DoesNotExist:
            messages.error(request, 'Equipment Does Not Exist.')
            return HttpResponseRedirect('/equipment/')



# fetch all users and pass them to template
@login_required(login_url='/login/')
def users(request):
    users = User.objects.all()
    context_dict = {'request': request, 'users': users}
    return render(request, "users.html", context_dict)

# function to hadle CRUD for Users
@login_required(login_url='/login/')
def user(request, userid=None):
    try:
        # determine if request is post or get
        if request.POST:
            try:
                # if id - update existing user with post data
                if userid:
                    try:
                        e = User.objects.get(id=userid)
                        updateuser = UserForm(request.POST, instance=e)
                        updateuser.save()
                        messages.success(request, 'User Updated Successfully')
                    except Exception as e:
                        messages.success(request, 'Error Updating User')
                        return HttpResponseRedirect('/users/')
                # if no id - create new user with post data
                else:
                    newuser = UserForm(request.POST)
                    e = newuser.save(commit=False)
                    e.save()
                    messages.success(request, 'User Added Successfully')
            except Exception as e:
                messages.error(request, 'Error Adding User.')
            return HttpResponseRedirect('/users/')
        else:
            # if id - view exisiting user and generate edit form
            if userid:
                try:
                    e = User.objects.get(id=userid)
                    form = UserForm(instance=e)
                    context_dict = {'user': e, 'form': form}
                    return render(request, "user.html", context_dict)
                except User.DoesNotExist:
                    messages.error(request, 'User Does Not Exist.')
                    return HttpResponseRedirect('/users/')
            # if no id - generate new user form
            else:
                form = UserForm()
                context_dict = {'form': form}
                return render(request, "user.html", context_dict)
    except Equipment.DoesNotExist:
            messages.error(request, 'User Does Not Exist.')
            return HttpResponseRedirect('/users/')

# get all departments and pass to template
@login_required(login_url='/login/')
def departments(request):
    departments = Department.objects.all()
    context_dict = {'request': request, 'departments': departments}
    return render(request, "departments.html", context_dict)



# function to handle CRUD for departments
@login_required(login_url='/login/')
def department(request, departmentid=None):
    try:
        # determine if request is post or get
        if request.POST:
            try:
                # if department id - update existing item with post data
                if departmentid:
                    try:
                        e = Department.objects.get(id=departmentid)
                        updatedepartment = DepartmentForm(request.POST, instance=e)
                        updatedepartment.save()
                        messages.success(request, 'Department Updated Successfully')
                    except Exception as e:
                        messages.success(request, 'Error Updating Department')
                        return HttpResponseRedirect('/departments/')
                # if no id - create new item with post data
                else:
                    newdepartment = DepartmentForm(request.POST)
                    e = newdepartment.save(commit=False)
                    e.save()
                    messages.success(request, 'Department Added Successfully')
            except Exception as e:
                messages.error(request, 'Error Adding Department.')
            return HttpResponseRedirect('/departments/')
        else:
            # if id - grab existing item and create form for edit
            if departmentid:
                try:
                    e = Department.objects.get(id=departmentid)
                    form = DepartmentForm(instance=e)
                    context_dict = {'department': e, 'form': form}
                    return render(request, "department.html", context_dict)
                except User.DoesNotExist:
                    messages.error(request, 'Department Does Not Exist.')
                    return HttpResponseRedirect('/departments/')
            # if no id - pass item create form to template
            else:
                form = DepartmentForm()
                context_dict = {'form': form}
                return render(request, "department.html", context_dict)
    except Equipment.DoesNotExist:
            messages.error(request, 'Department Does Not Exist.')
            return HttpResponseRedirect('/departments/')

# pull all manufacturers and pass to template
@login_required(login_url='/login/')
def manufacturers(request):
    manufacturers = Manufacturer.objects.all()
    context_dict = {'request': request, 'manufacturers': manufacturers}
    return render(request, "manufacturers.html", context_dict)

# handles CRUD for all Manufacturer items
@login_required(login_url='/login/')
def manufacturer(request, manufacturerid=None):
    try:
        # determine if request is post / get
        if request.POST:
            try:
                # if id exists - update existing item with post data
                if manufacturerid:
                    try:
                        e = Manufacturer.objects.get(id=manufacturerid)
                        updatemanufacturer = ManufacturerForm(request.POST, instance=e)
                        updatemanufacturer.save()
                        messages.success(request, 'Manufacturer Updated Successfully')
                    except Exception as e:
                        messages.success(request, 'Error Updating Manufacturer')
                        return HttpResponseRedirect('/manufacturers/')
                # if no id - create new item with post data
                else:
                    newmanufacturer = ManufacturerForm(request.POST)
                    e = newmanufacturer.save(commit=False)
                    e.save()
                    messages.success(request, 'Department Added Successfully')
            except Exception as e:
                messages.error(request, 'Error Adding Manufacturer.')
            return HttpResponseRedirect('/manufacturers/')
        else:
            # if id exists - grab existing item and pass edit form
            if manufacturerid:
                try:
                    e = Manufacturer.objects.get(id=manufacturerid)
                    form = ManufacturerForm(instance=e)
                    context_dict = {'department': e, 'form': form}
                    return render(request, "manufacturer.html", context_dict)
                except User.DoesNotExist:
                    messages.error(request, 'Manufacturer Does Not Exist.')
                    return HttpResponseRedirect('/manufacturers/')
            # if no id - pass create form to template
            else:
                form = ManufacturerForm()
                context_dict = {'form': form}
                return render(request, "manufacturer.html", context_dict)
    except Equipment.DoesNotExist:
            messages.error(request, 'Manufacturer Does Not Exist.')
            return HttpResponseRedirect('/manufacturers/')
