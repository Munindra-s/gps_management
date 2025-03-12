from django.db import models

# Create your models here.    
class customer_master(models.Model):
    customer_id=models.CharField(max_length=20,unique=True)
    customer_name=models.CharField(max_length=30)
    phone=models.IntegerField()
    status=models.IntegerField(default=1)

class customer_details(models.Model):
    customer_id=models.CharField(max_length=20)
    customer_name=models.CharField(max_length=30)
    phone=models.IntegerField()
    email_id=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    status=models.IntegerField(default=1)

class gps_master(models.Model):
    gps_id=models.CharField(max_length=50,unique=True)
    customer_name=models.CharField(max_length=40)
    imei_no=models.IntegerField()
    vehicle_registration_no=models.CharField(max_length=20)
    vehicle_model=models.DateField( auto_now=False, auto_now_add=False)
    vehicle_make=models.DateField( auto_now=False, auto_now_add=False)
    vehicle_type=models.CharField( max_length=50)
    status=models.IntegerField(default=1)

class gps_details(models.Model):
    gps_id=models.CharField(max_length=50)
    customer_name=models.CharField(max_length=40)
    imei_no=models.IntegerField()
    vehicle_registration_no=models.CharField(max_length=20)
    vehicle_model=models.DateField( auto_now=False, auto_now_add=False)
    vehicle_make=models.DateField( auto_now=False, auto_now_add=False)
    vehicle_type=models.CharField( max_length=50)
    installation_date=models.DateField(auto_now=False, auto_now_add=False)
    reminder_date=models.DateField(auto_now=False, auto_now_add=False)
    next_reminder_date=models.DateField(auto_now=False, auto_now_add=False)
    plan=models.CharField(max_length=40)
    status=models.IntegerField(default=1)

