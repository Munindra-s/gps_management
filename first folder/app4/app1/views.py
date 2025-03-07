from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from app1.models import add_customer,add_enquiry,add_gps,add_insurance
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout


# Create your views here.
def add_cust(request):
        if request.method =='POST':
              name=request.POST['name']
              customer=request.POST['customer_id']
              phone=request.POST['phone']
              email=request.POST['email']
              address=request.POST['address']
              vehicle_no=request.POST['vehicle_no']
              insurance_id=request.POST['insurance id']
              date=request.POST['date']
              vehicle_type=request.POST['vehicle type']
              policy_type=request.POST['policy type']
              policy_amount=request.POST['policy Amount']
              start_date=request.POST['insurance Start Date']
              end_date=request.POST['insurance End Date']
              reminder_date=request.POST['reminder Date']
              add_customer.objects.create(name=name,customer_id=customer,phone=phone,email=email,address=address,vehicle_no=vehicle_no,insurance_id=insurance_id,date=date,vehicle_type=vehicle_type,policy_type=policy_type,policy_amount=policy_amount,insurance_start_date=start_date,insurance_end_date=end_date,reminder_date=reminder_date)     
              return redirect("add_customer")
        last_customer = add_customer.objects.order_by('-customer_id').first()
        if last_customer:
            last_id = int(last_customer.customer_id[4:])  # Extract the numeric part
            new_id = f"SSDC{last_id + 1:04d}"
            print('*****',new_id)
        else:
            new_id = "SSDC0001"
        context={'new_id':new_id}
              
        return render(request,'add_customer.html',context)

def list_customer(request):
        data=add_customer.objects.all()
        context={'sent':data}
        return render(request,'list_customer.html',context)
@login_required
def add_enquiries(request):
        if request.method =='POST':
                name=request.POST['name']
                customer=request.POST['customer id']
                phone=request.POST['phone']
                registration_no=request.POST['registration no']
                vehicle_model=request.POST['vehicle model']
                manufacturing_year=request.POST['manufacturing year']
                previous_policy_no=request.POST['previous policy no']
                insurance_name=request.POST['insurance name']
                vehicle_type=request.POST['vehicle type']
                expiry_date=request.POST['expiry date']
                start_date=request.POST['star date']
                end_date=request.POST['end_date']
                add_enquiry.objects.create(name=name,customer_id=customer,phone=phone,registration_no=registration_no,vehicle_model=vehicle_model,manufacturing_year=manufacturing_year,previous_policy_no=previous_policy_no,insurance_name=insurance_name,vehicle_type=vehicle_type,expiry_date=expiry_date,start_date=start_date,end_date=end_date)

                return render(request,'add_enquiry.html')
        return render(request,'add_enquiry.html')
def list_enquiry(request):
        value=add_enquiry.objects.all()
        context={'sent':value}
        return render(request,'list_enquiry.html',context)
@login_required
def add_gps_management(request):
        if request.method =='POST':
                vehicle_id=request.POST['vehicle_id']
                vehicle_model=request.POST['vehicle_model']
                vehicle_registration_no=request.POST['vehicle_registration_no']
                vehicle_type=request.POST['vehicle_type']
                vehicle_make=request.POST['vehicle_make']
                add_gps.objects.create(vehicle_id=vehicle_id,vehicle_model=vehicle_model,vehicle_registration_no=vehicle_registration_no,vehicle_type=vehicle_type,vehicle_make=vehicle_make)

        return render(request,'add_gps.html') 
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

def add_insurancesss(request):
        if request.method =='POST':
                name=request.POST['name']
                customer_id=request.POST['customer_id']
                phone=request.POST['phone']
                registration_no = request.POST['registration_no']
                vehicle_model=request.POST['vehicle_model']
                year=request.POST['year']
                policy_no=request.POST['policy_no']
                insurance_name=request.POST['insurance_name']
                vehicle_type=request.POST['vehicle_type']
                expiry_date = request.POST['expiry_date']
                start_date=request.POST['start_date']
                end_date=request.POST['end_date']
                daa = add_insurance.objects.create(name=name,customer_id=customer_id,phone=phone,registration_no=registration_no,vehicle_model=vehicle_model,year=year,policy_no=policy_no,insurance_name=insurance_name,vehicle_type=vehicle_type,expiry_date=expiry_date,start_date=start_date,end_date=end_date)

        return render(request,'add_insurance.html')

def list_insurance(request):
        part=add_insurance.objects.all()
        concept={'sent':part}
        return render(request,'list_insurance.html',concept)



