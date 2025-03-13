from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from app1.models import customer_master,enquiry_details,add_gps,customer_details,insurance_master,insurance_details
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout


# Create your views here.
def add_customer(request):
        if request.method =='POST':
              name=request.POST['name']
              customer=request.POST['customer_id']
              phone=request.POST['phone']
              email=request.POST['email']
              address=request.POST['address']
              
              customer_master.objects.create(name=name,customer_id=customer,phone=phone,email=email,address=address,)     
              return redirect("add_customer")
        last_customer = customer_master.objects.order_by('-customer_id').first()
        if last_customer:
            last_id = int(last_customer.customer_id[4:])  # Extract the numeric part
            new_id = f"SSDC{last_id + 1:04d}"
            iiii = f"SSDC{last_id + 1:04d}"
            print(iiii)
            print('*****',new_id)
        else:
            new_id = "SSDC0001"
        context={'new_id':new_id}
              
        return render(request,'add_customer.html',context)

def list_customer(request):
        data=customer_master.objects.all()
        context={'sent':data}
        return render(request,'list_customer.html',context)

def add_details(request):
       if request.method =='POST':
              name=request.POST['name']
              customer=request.POST['customer_id']
              phone=request.POST['phone']
              email=request.POST['email']
              address=request.POST['address']
              customer_details.objects.create(name=name,customer_id=customer,phone=phone,email=email,address=address,)   
              
              

def add_enquiries(request):
        if request.method =='POST':
                name=request.POST['name']
                enquiry_id=request.POST['enquiry_id']
                phone=request.POST['phone']
                vehicle_no=request.POST['vehicle_no']
                reference_of_enquiry=request.POST['reference_of_enquiry']
                vehicle_model=request.POST['vehicle_model']
                manufacturing_year=request.POST['manufacturing_year']
                previous_policy_no=request.POST['previous_policy_no']
                insurance_name=request.POST['insurance_name']
                vehicle_type=request.POST['vehicle_type']
                expiry_date=request.POST['expiry_date']
                start_date=request.POST['start_date']
                end_date=request.POST['end_date']
                enquiry_details.objects.create(name=name,enquiry_id=enquiry_id,phone=phone,vehicle_no=vehicle_no,reference_of_enquiry=reference_of_enquiry,vehicle_model=vehicle_model,manufacturing_year=manufacturing_year,previous_policy_no=previous_policy_no,insurance_name=insurance_name,vehicle_type=vehicle_type,expiry_date=expiry_date,start_date=start_date,end_date=end_date)
                return redirect('list_enquiry')
        last_enquiry = enquiry_details.objects.order_by('-enquiry_id').first()
        if last_enquiry:
            last_id = int(last_enquiry.enquiry_id[3:])  # Extract the numeric part
            new_id = f"ENQ{last_id + 1:04d}"
            print('*****',new_id)
        else:
            new_id = "ENQ0001"
        context={'new_id':new_id}
               
        return render(request,'add_enquiry.html',context)
        
        
def list_enquiry(request):
        value=enquiry_details.objects.all()
        context={'sent':value}
        return render(request,'list_enquiry.html',context)

def add_gps_management(request):
        if request.method =='POST':
                Gps_device_IMEI_no=request.POST['Gps_device_IMEI_no']
                registration_no=request.POST['registration_no']
                install_date=request.POST['install_date']
                renew_date=request.POST['renew_date']
                reminder_date=request.POST['reminder_date']
                vehicle_model=request.POST['vehicle_model']
                vehicle_type=request.POST['vehicle_type']
                vehicle_make=request.POST['vehicle_make']
                add_gps.objects.create(Gps_device_IMEI_no=Gps_device_IMEI_no,registration_no=registration_no,vehicle_model=vehicle_model,vehicle_type=vehicle_type,vehicle_make=vehicle_make,install_date=install_date,reminder_date=reminder_date,renew_date=renew_date)
        data=customer_master.objects.all()
        context={'sent':data}

        return render(request,'add_gps.html',context) 


def list_gps_management(request):
        content=add_gps.objects.all()
        context={'sent':content}
        return render(request,'list_gps.html',context)  
 
def add_sign_class(request):
        if request.method =='POST':
                username=request.POST['username']
                password=request.POST['password']
                user=authenticate(username=username,password=password) 
                if user is not None:
                        login(request,user)
                        return redirect('add_gps')
                else:
                        return render(request,'class.html')
        return render(request,'class.html')

def sign_out(request):
        logout(request)
        return redirect('class')

def city_autocomplete(request):
    data = add_customer.objects.all()
    context = {'sent':data}
    # Add_Insurance;.objects.create(invoice_number = 1, customer_name = "Test", date = "25-10-2001", total_amount = 1000)

    return render(request,'render.html', context) 

def add_insurance(request):
       
        if request.method =='POST':

                customer_details=request.POST['customer_details']
                print(customer_details)
                name, phone = customer_details.split(' --- ')

                
                
                insurance_id=request.POST['insurance_id']
                registration_no = request.POST['registration_no']
                vehicle_model=request.POST['vehicle_model']
                year=request.POST['year']
                policy_no=request.POST['policy_no']
                expiry_date=request.POST['expiry_date']
                vehicle_type=request.POST['vehicle_type']
                start_date=request.POST['start_date']
                end_date=request.POST['end_date']
                daa =insurance_master.objects.create(name=name,insurance_id=insurance_id,registration_no=registration_no,vehicle_model=vehicle_model,year=year,)
                insurance_details.objects.create(insurance_id=insurance_id,name=name,phone=phone,registration_no=registration_no,vehicle_model=vehicle_model,expiry_date=expiry_date,year=year,policy_no=policy_no,vehicle_type=vehicle_type,start_date=start_date,end_date=end_date)
                return redirect('path_insurance') 

                 
        last_insurance = insurance_details.objects.order_by('-insurance_id').first()
        if last_insurance:
            last_id = int(last_insurance.insurance_id[3:])  # Extract the numeric part
            new_id = f"INS{last_id + 1:04d}"
            print('*****',new_id)
            
        else:
            new_id = "INS0001"
        data=customer_master.objects.all()    
        context={'new_id':new_id,'sent':data}
              
        return render(request,'add_insurance.html',context)
     

def list_insurance(request):
        part=insurance_details.objects.filter(status=1)
        context={'sent':part}
        return render(request,'list_detail.html',context)


       



# def town_autocomplete(request):
#     data = add_gps.objects.all()
#     context = {'sent':data}
#     # Add_Insurance;.objects.create(invoice_number = 1, customer_name = "Test", date = "25-10-2001", total_amount = 1000)

#     return render(request,'add_gps.html', context) 




