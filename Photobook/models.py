from operator import truth
from re import T
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Photobook(models.Model):
    co_id = models.IntegerField(primary_key=True)
    order_number = models.CharField(max_length=500)
    page_details = models.JSONField(max_length=500)
    version = models.CharField(max_length=500)
    created_at = models.DateField()
    updated_at = models.DateField() 