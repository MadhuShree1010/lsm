from django.urls import path
from . import views

urlpatterns=[
    path("",views.teamleader,name="teamLeader"),
    path("",views.teamMember,name="teamMember"),
]