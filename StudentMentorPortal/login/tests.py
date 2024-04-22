from django.test import TestCase

# Create your tests here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(min_length=6)


class Mentor(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    experience = models.CharField(max_length=50)


