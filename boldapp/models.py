from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    organizationaltag = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.PROTECT)
    manufacturerpartnum = models.CharField(max_length=100)
    department = models.ForeignKey('Department', on_delete=models.PROTECT)
    officelocation = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    accountnumber = models.CharField(max_length=100)
    accountmanager = models.CharField(max_length=100)
    supportnumber = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    supervisor = models.CharField(max_length=100)
    phonenumber =models.CharField(max_length=100)

    def __str__(self):
        return self.name
