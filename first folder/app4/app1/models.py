from django.db import models

# Create your models here.    
class customer_master(models.Model):
    customer_id=models.CharField(max_length=20)
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

class add_gps(models.Model):
    gps_id=models.CharField(max_length=50)
    customer_name=models.CharField(max_length=40)
    imei_no=models.IntegerField()
    vehicle_registration_no=models.CharField(max_length=20)
    vehicle_model=models.DateField( auto_now=False, auto_now_add=False)
    vehicle_make=models.DateField( auto_now=False, auto_now_add=False)
    vehicle_type=models.CharField( max_length=50)
    status=models.IntegerField(default=1)

# class gps_details(models.Model):


class add_enquiry(models.Model):
    customer_id=models.CharField( max_length=50)
    name=models.CharField( max_length=50)
    phone=models.CharField( null=True,max_length=50)
    registration_no=models.CharField( max_length=50)
    vehicle_model=models.DateField( auto_now=False, auto_now_add=False)
    manufacturing_year=models.DateField( auto_now=False, auto_now_add=False)
    previous_policy_no=models.IntegerField()
    insurance_name=models.CharField( max_length=50)
    expiry_date=models.DateField( auto_now=False, auto_now_add=False)
    vehicle_type=models.CharField( max_length=50)
    start_date=models.DateField( auto_now=False, auto_now_add=False)
    end_date=models.DateField( auto_now=False, auto_now_add=False)

class add_insurance(models.Model):
    customer_id=models.CharField( max_length=60)
    name=models.CharField( max_length=50)
    phone=models.CharField( null=True,max_length=50)
    registration_no=models.CharField( max_length=50)
    vehicle_model=models.DateField( auto_now=False, auto_now_add=False)
    year=models.DateField( auto_now=False, auto_now_add=False,null=True)
    policy_no=models.IntegerField()
    insurance_name=models.CharField( max_length=50)
    expiry_date=models.DateField( auto_now=False, auto_now_add=False)
    vehicle_type=models.CharField( max_length=50)
    start_date=models.DateField( auto_now=False, auto_now_add=False)
    end_date=models.DateField( auto_now=False, auto_now_add=False)

    




    









