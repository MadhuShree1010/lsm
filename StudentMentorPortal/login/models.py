from django.db import models


class Student(models.Model):
    Username = models.CharField(max_length=50,unique=True)
    password = models.CharField(min_length=6)
    leader = models.BooleanField(default=False)


class Mentor(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=20,unique=True)
    experience = models.CharField(max_length=50)
