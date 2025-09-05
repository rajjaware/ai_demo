from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Inherit username/password, etc.

class Rule(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Device(models.Model):
    name = models.CharField(max_length=100)
    inventory_type = models.CharField(max_length=50)  # 'InventoryM' or 'SWIMM'
    icmm_rules = models.ArrayReferenceField(to=Rule, blank=True)

class OS(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=50)

class Usecase(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    type = models.CharField(max_length=4, choices=[('PRE', 'Pre'), ('POST', 'Post')])
    steps = models.TextField()