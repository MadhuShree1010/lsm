from django.urls import path
from . import views

urlpatterns=[
    path("header", views.teamLeader, name="teamLeader"),
    path("header2", views.teamMember, name="teamMember"),
    path("todo", views.todo, name="todo"),
    path("mentors", views.mentors, name="mentors"),
    path("diary", views.diary, name="diary"),
    path("assign-task", views.assignTask, name="assignTask"),
]
