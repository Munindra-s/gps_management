from django.db import models

# Create your models here.
class customer_master(models.Model):
    customer_id=models.CharField( max_length=50)
    name=models.CharField( max_length=50)
    phone=models.CharField( null=True,max_length=50)  
    email=models.CharField( max_length=50)
    address=models.CharField( max_length=50)

class customer_details(models.Model):
    customer_id=models.CharField( max_length=50)
    name=models.CharField( max_length=50)
    phone=models.IntegerField()
    vehicle_details=models.CharField( max_length=50)
    insurance_id=models.CharField( max_length=50)
    customer_name=models.CharField( max_length=50)




    


class enquiry_details(models.Model):
    enquiry_id=models.CharField( max_length=50,unique=True)
    name=models.CharField( max_length=50)
    phone=models.CharField( null=True,max_length=50)
    vehicle_no=models.CharField( max_length=50)
    reference_of_enquiry=models.CharField( max_length=50)
    vehicle_model=models.DateField( auto_now=False, auto_now_add=False)
    manufacturing_year=models.DateField( auto_now=False, auto_now_add=False)
    previous_policy_no=models.IntegerField()
    insurance_name=models.CharField( max_length=50)
    expiry_date=models.DateField( auto_now=False, auto_now_add=False)
    vehicle_type=models.CharField( max_length=50)
    start_date=models.DateField( auto_now=False, auto_now_add=False)
    end_date=models.DateField( auto_now=False, auto_now_add=False)
    status=models.IntegerField(default=1,null=True)


class add_gps(models.Model):
    Gps_device_IMEI_no=models.IntegerField(null=True)
    install_date=models.DateField( auto_now=False, auto_now_add=False,null=True)
    renew_date=models.DateField( auto_now=False, auto_now_add=False,null=True)
    reminder_date=models.DateField( auto_now=False, auto_now_add=False,null=True)
    registration_no=models.CharField( max_length=50)
    vehicle_model=models.DateField( auto_now=False, auto_now_add=False)
    vehicle_make=models.DateField( auto_now=False, auto_now_add=False)
    vehicle_type=models.CharField( max_length=50)


class insurance_master(models.Model):
    insurance_id=models.CharField( max_length=60,unique=True)
    name=models.CharField( max_length=50)
    registration_no=models.CharField( max_length=50)
    vehicle_model=models.DateField( auto_now=False, auto_now_add=False)
    year=models.DateField( auto_now=False, auto_now_add=False,null=True)
    status=models.IntegerField(default=1,null=True)
    

class insurance_details(models.Model):
    insurance_id=models.CharField( max_length=60)
    name=models.CharField( max_length=50)
    phone=models.IntegerField(null=True)
    registration_no=models.CharField( max_length=50,null=True)
    vehicle_model=models.DateField( auto_now=False, auto_now_add=False,null=True)
    year=models.DateField( auto_now=False, auto_now_add=False,null=True)
    policy_no=models.IntegerField(null=True)
    expiry_date=models.DateField( auto_now=False, auto_now_add=False,null=True)
    vehicle_type=models.CharField( max_length=50,null=True)
    start_date=models.DateField( auto_now=False, auto_now_add=False,null=True)
    end_date=models.DateField( auto_now=False, auto_now_add=False,null=True)
    status=models.IntegerField(default=1,null=True)










    









