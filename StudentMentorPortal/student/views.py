import json
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_protect, csrf_exempt, requires_csrf_token
from . import models


def teamMember(request):
    return render(request,"header.html")


def teamLeader(request):
    return render(request,"header2.html")

def todo(request):
    return render(request,"todo.html")

def mentors(request):
    return render(request,"mentor.html")


def diary(request):
    return render(request,"diary.html")

def Task(request):
    return render(request,"task.html")



