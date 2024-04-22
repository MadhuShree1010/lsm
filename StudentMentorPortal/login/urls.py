from django.urls import path
from . import views

urlpatterns=[
    path("",views.landingPage,name="landingPage"),
    path("mentor",views.mentorpage,name="MentorPage"),
    path("login",views.loginPage,name="LoginPage"),
    path("signup",views.signUpPage,name="signUpPage"),
]