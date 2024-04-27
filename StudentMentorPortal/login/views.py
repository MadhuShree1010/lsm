import json
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_protect, csrf_exempt, requires_csrf_token



def landingPage(request):
    return render(request,"index.html")

def loginPage(request):
    return render(request,"login.html")

def signUpPage(request):
    return render(request,"signup.html")

def mentorpage(request):
    return render(request,"mentor_registration.html")







