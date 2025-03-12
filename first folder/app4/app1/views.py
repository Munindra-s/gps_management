from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from app1.models import customer_master,customer_details,gps_master,gps_details
from django.contrib.auth.models import User


# Create your views here.
def custmas(request):
        if request.method=='POST':
                customer_id=request.POST['customer_id']
                name=request.POST['name']
                phone=request.POST['phone']
                email_id=request.POST['email']
                address=request.POST['address']
                customer_master.objects.create(customer_name=name,customer_id=customer_id,phone=phone)
                customer_details.objects.create(customer_name=name,customer_id=customer_id,phone=phone,email_id=email_id,address=address)
                return redirect('list_customer')
        last_customer = customer_details.objects.order_by('-customer_id').first()
        if last_customer:
                last_id = int(last_customer.customer_id[4:])  # Extract the numeric part
                new_id = f"CUST{last_id + 1:04d}"
                print(new_id)
        else:
                new_id = "CUST0001"
        context={'new_id':new_id}
        return render(request,"add_customer.html",context)

       
def list_customer(request):
        data=customer_details.objects.filter(status=1)
        context={'sent':data}
        return render(request,'list_customer.html',context)

@login_required
def add_gps_management(request):
        if request.method =='POST':
                gps_id=request.POST['gps_id']              
                imei_no=request.POST['imei_no']
                vehicle_registration_no=request.POST['vehicle_registration_no']
                vehicle_model=request.POST['vehicle_model']
                vehicle_make=request.POST['vehicle_make']
                vehicle_type=request.POST['vehicle_type']
                installation_date=request.POST['installation_date']
                reminder_date=request.POST['reminder_date']
                next_reminder_date=request.POST['next_reminder_date']
                plan=request.POST['plan']
                gps_master.objects.create(gps_id=gps_id,customer_name='ii',imei_no=imei_no,vehicle_registration_no=vehicle_registration_no,vehicle_model=vehicle_model,vehicle_make=vehicle_make,vehicle_type=vehicle_type)
                gps_details.objects.create(gps_id=gps_id,customer_name='ii',imei_no=imei_no,vehicle_registration_no=vehicle_registration_no,vehicle_model=vehicle_model,vehicle_make=vehicle_make,vehicle_type=vehicle_type,installation_date=installation_date,reminder_date=reminder_date,next_reminder_date=next_reminder_date,plan=plan)
                return redirect('list_gps') 
        orderby_id=gps_details.objects.order_by('-gps_id').first()
        if orderby_id:
                old_id=int(orderby_id.gps_id[3:])
                fresh_id=f"GPS{old_id+1:04d}"
                print(fresh_id)
        else:
             fresh_id="GPS0001"
        data=customer_details.objects.all()
        context={'fresh_id':fresh_id,'sent':data}
        return render(request,"add_gps.html",context)

def list_gps_management(request):
        content=gps_master.objects.filter(status=1)
        context={'sent':content}
        return render(request,'list_gps.html',context)


