from django.db import models

# Create your models here.
class add_customer(models.Model):
    customer_id=models.CharField( max_length=50)
    name=models.CharField( max_length=50)
    phone=models.CharField( null=True,max_length=50)  
    email=models.CharField( max_length=50)
    address=models.CharField( max_length=50)
    insurance_id=models.IntegerField()
    vehicle_no=models.CharField( max_length=50)
    date=models.DateField( auto_now=False, auto_now_add=False)
    vehicle_type=models.CharField( max_length=50)
    policy_type=models.CharField( max_length=50)
    policy_amount=models.IntegerField()
    insurance_start_date=models.DateField( auto_now=False, auto_now_add=False)
    insurance_end_date=models.DateField( auto_now=False, auto_now_add=False)
    reminder_date=models.DateField( auto_now=False, auto_now_add=False)

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


class add_gps(models.Model):
    Gps_device_IMEI_no=models.IntegerField(null=True)
    install_date=models.DateField( auto_now=False, auto_now_add=False,null=True)
    renew_date=models.DateField( auto_now=False, auto_now_add=False,null=True)
    reminder_date=models.DateField( auto_now=False, auto_now_add=False,null=True)
    registration_no=models.CharField( max_length=50)
    vehicle_model=models.DateField( auto_now=False, auto_now_add=False)
    vehicle_make=models.DateField( auto_now=False, auto_now_add=False)
    vehicle_type=models.CharField( max_length=50)


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








    









