from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from project3.models import User, Equipment, Department, Manufacturer
# from project3.forms import UserForm, EquipmentForm, DepartmentForm, ManufacturerForm
import urllib2
import json
from bold.forms import GenderPredictionForm

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

    req = urllib2.Request(url, body, headers)
    testresult = 0
    try:
        response = urllib2.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers)
        # response = urllib.request.urlopen(req)



        result = response.read()
        testresult = json.loads(result)
        output = testresult['Results']['output1']['value']['Values'][0][7]
    except urllib2.HTTPError, error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())

        print(json.loads(error.read()))


    return JsonResponse({'result': output})

