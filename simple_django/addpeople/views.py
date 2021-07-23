from django.core.checks.messages import Error
from django.db import connections
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


from .models import People
import json
import uuid

# Create your views here.
def index(request):
    return HttpResponse(request)

def postPerson(request):
    try:
        bodyInBytes = request.body
        bodyInJson = json.loads(bodyInBytes.decode('utf8'))

        if(People.objects.filter(firstName=bodyInJson["firstName"],lastName=bodyInJson["lastName"])):
            return HttpResponse("Person already exists")
        p = People(firstName=bodyInJson["firstName"],lastName=bodyInJson["lastName"],age=bodyInJson["age"],sex=bodyInJson["sex"],createdBy=bodyInJson["user"])
        p.save()
        return HttpResponse("Success")
    except Exception as e:
        print(e)
        return HttpResponse(str(e))

def getPeople(request,id=0):
    peps = People.objects.filter(createdBy=id)
    print(peps)
    return HttpResponse(peps)

    