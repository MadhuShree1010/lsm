import json
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_protect, csrf_exempt, requires_csrf_token
from . import models
from django.shortcuts import render, redirect
from .models import diary


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




def save_entry(request):
    if request.method == 'POST':
        entry_text = request.POST.get('entry')
        if entry_text:
            diary.objects.create(entry=entry_text)
    return redirect('header')  # Redirect to a relevant URL after saving the entry
