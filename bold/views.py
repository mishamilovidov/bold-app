from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from project3.models import User, Equipment, Department, Manufacturer
# from project3.forms import UserForm, EquipmentForm, DepartmentForm, ManufacturerForm
# import urllib2
# from urllib.request import urlopen, Request
import urllib
import urllib3
import json
import codecs
from bold.forms import GenderPredictionForm, MatchboxForm

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

    genderform = GenderPredictionForm()

    context_dict = {'request': request, 'genderform': genderform}
    return render(request, "prediction.html", context_dict)


def experiment(request):

    facebook = request.GET.get('facebook', None)
    pinterest = request.GET.get('pinterest', None)
    pandora = request.GET.get('pandora', None)
    espn = request.GET.get('espn', None)
    linkedin = request.GET.get('linkedin', None)

    facebook = str(facebook)
    pintrest = str(pinterest)
    pandora = str(pandora)
    espn = str(espn)
    linkedin = str(linkedin)
    test = "1"

    data = {

        "Inputs": {

            "input1":
                {
                    "ColumnNames": ["user_id", "facebook", "instagram", "drawsomething", "templerun", "clashofclans",
                                    "wwffree", "pinterest", "pandora", "espn", "linkedin", "twitter", "netflix",
                                    "groupon", "newyorktimes", "gender", "carrier"],
                    "Values": [
                        ["0", facebook, "0", "0", "0", "0", "0", pinterest, pandora, espn, linkedin, "0", "0", "0", "0", "0", "value"],
                        ["0", facebook, "0", "0", "0", "0", "0", pinterest, pandora, espn, linkedin, "0", "0", "0", "0", "0", "value"], ]
                }, },
        "GlobalParameters": {
        }
    }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/82e21ff375ba4d35800059164b8a2e64/services/3dd5dad3429b4f52bf9035936a87c75b/execute?api-version=2.0&details=true'
    api_key = 'qfWmNpQ6lyTFQ1ZLEbRgCaXnXKhXToVkEWDVfmu1NkJsG+xHj0x0yBvbhQxjrqacw7NOMuJUcEgDG7eD2XrjNg=='  # Replace this with the API key for the web service
    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}


    # req = urllib.request.Request(url, body, headers)



    http = urllib3.PoolManager()



    r = http.request('POST', url, body=body, headers=headers)

    # body = r.data.read().decode('utf-8')

    testresult = json.loads(str(r.data))

    # try:
    #     with open(r.data['Results']['output1']['value']['Values']) as test:
    #         testresult = json.load(test)
    # except Exception as e:
    #     print(e)
    # print(testresult)
    output = testresult['Results']['output1']['value']['Values'][0][7]
    # print(output)

    # print(testresult)



    return JsonResponse({'result': output})


@login_required(login_url='/login/')
def matchbox(request):

    matchboxform = MatchboxForm()

    context_dict = {'request': request, 'genderform': matchboxform}
    return render(request, "matchbox.html", context_dict)


def matchbox_handler(request):


    facebook = request.GET.get('facebook', None)
    instagram = request.GET.get('instagram', None)
    drawsomething = request.GET.get('drawsomething', None)
    templerun = request.GET.get('templerun', None)
    clashofclans = request.GET.get('clashofclans', None)
    wwffree = request.GET.get('wwffree', None)
    pinterest = request.GET.get('pinterest', None)
    pandora = request.GET.get('pandora', None)
    zombiefarm = request.GET.get('zombiefarm', None)

    facebook = str(facebook)
    instagram = str(instagram)
    drawsomething = str(drawsomething)
    templerun = str(templerun)
    clashofclans = str(clashofclans)
    wwffree = str(wwffree)
    pinterest = str(pinterest)
    pandora = str(pandora)
    zombiefarm = str(zombiefarm)



    data = {

        "Inputs": {

            "input1":
                {
                    "ColumnNames": ["user_id", "facebook", "instagram", "drawsomething", "templerun", "clashofclans",
                                    "wwffree", "pinterest", "pandora", "zombiefarm"],
                    "Values": [["0", facebook, instagram, drawsomething, templerun, clashofclans, wwffree, pinterest, pandora, zombiefarm],
                               ["0", facebook, instagram, drawsomething, templerun, clashofclans, wwffree, pinterest, pandora, zombiefarm], ]
                }, },
        "GlobalParameters": {
        }
    }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/82e21ff375ba4d35800059164b8a2e64/services/222e14fe70d1466f943ad64889827fa0/execute?api-version=2.0&details=true'
    api_key = 'G0ucwzaDyKli+3s8K3KcHkGSAm4qrAnhIRQK31QCORAhNnazcMtYHou9Evvr7dbzoiejICH4/v2O1rJfLDHVmQ=='  # Replace this with the API key for the web service
    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}



    http = urllib3.PoolManager()

    r = http.request('POST', url, body=body, headers=headers)

    testresult = json.loads(r.data)

    print(testresult)
    output = testresult['Results']['output1']['value']['Values'][0][7]
    print(output)



    return JsonResponse({'result': output})