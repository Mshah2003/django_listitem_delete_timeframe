from django.db import models
from datetime import datetime

# Create your models here.

class Date(models.Model):
    title = models.CharField(max_length=10)
    date = models.DateField(blank=True)