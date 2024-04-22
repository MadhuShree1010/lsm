from django.db import models


class task(models.Model):
    work = models.TextField(max_length=220)
    date = models.DateField
    completed  = models.BooleanField

class diary(models.Model):
    date = models.DateField(auto_now_add=True)
    entry = models.TextField(max_length=500)