from django.db import models

class ClientData(models.Model):
    phone = models.CharField(max_length=11, blank=False, default='')
    fullname = models.CharField(max_length=50,blank=False, default='')
    address = models.CharField(max_length=50,blank=False, default='')
    email = models.CharField(max_length=30,blank=False, default='')

class OrderData(models.Model):
    phone = models.CharField(max_length=11, blank=False, default='')
    fullname = models.CharField(max_length=50,blank=False, default='')
    address = models.CharField(max_length=50,blank=False, default='')
    email = models.CharField(max_length=30,blank=False, default='')
    item = models.CharField(max_length=15,blank=False, default='GALLON 1')
    quantity = models.IntegerField(blank=True, null=True)
    payment = models.IntegerField(blank=True, null=True)
    reservationDate = models.DateTimeField()

class OrderStatus(models.Model):
    phone = models.CharField(max_length=11, blank=False, default='')
    fullname = models.CharField(max_length=50,blank=False, default='')
    address = models.CharField(max_length=50,blank=False, default='')
    email = models.CharField(max_length=30,blank=False, default='')
    item = models.CharField(max_length=15,blank=False, default='GALLON 1')
    quantity = models.IntegerField(blank=True, null=True)
    payment = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=15,blank=False, default='Preparing')

class Order_stats_sales(models.Model):
    item = models.CharField(max_length=15,blank=False, default='GALLON 1')
    price = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField()
