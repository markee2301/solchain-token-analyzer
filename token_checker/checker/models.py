# models.py

from django.db import models

class Token(models.Model):
    address = models.CharField(max_length=100)
