from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField('Address')
    nit = models.CharField(max_length=11)

class Ticket(models.Model):
    plate_num = models.CharField(max_length=8)
    check_in = models.DateTimeField('Check-in')
    check_out = models.DateTimeField('Check-out')
    total = models.DecimalField(max_digits=5, decimal_places=2)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    status = models.BooleanField(default=0)
