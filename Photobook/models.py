from django.db import models
from django.utils import timezone

# Create your models here.
class Photobook(models.Model):
    co_id = models.AutoField(primary_key=True, unique=True)
    order_number = models.CharField(max_length=500)
    page_details = models.JSONField(max_length=500)
    version = models.CharField(max_length=500)
    created_at = models.DateField(timezone.now)
    updated_at = models.DateField(timezone.now) 