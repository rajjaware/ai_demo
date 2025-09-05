from django.db import models

class Rule(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Device(models.Model):
    name = models.CharField(max_length=100)
    inventory_type = models.CharField(max_length=50)  # e.g., InventoryM or SWIMM
    icmm_rules = models.ManyToManyField(Rule, blank=True)

class OS(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    os_name = models.CharField(max_length=100)
    os_version = models.CharField(max_length=50)

class Usecase(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=[('PRE', 'Pre'), ('POST', 'Post')])
    steps = models.TextField()