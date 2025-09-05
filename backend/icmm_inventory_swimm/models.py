from django.db import models

class Rule(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Device(models.Model):
    name = models.CharField(max_length=100)
    inventory_type = models.CharField(max_length=50)  # 'InventoryM' or 'SWIMM'
    icmm_rules = models.ManyToManyField(Rule, blank=True, related_name="devices")

class OS(models.Model):
    device = models.OneToOneField(Device, on_delete=models.CASCADE, related_name="os")
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=50)

class Usecase(models.Model):
    PRE = 'PRE'
    POST = 'POST'
    TYPE_CHOICES = [(PRE, 'Pre'), (POST, 'Post')]

    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="usecases")
    type = models.CharField(max_length=4, choices=TYPE_CHOICES)
    steps = models.TextField()