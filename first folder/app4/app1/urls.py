from django.urls import path
from . import views
urlpatterns =[
    path('add_customer/',views.add_customer,name='add_customer'),
    path('list_customer/',views.list_customer,name='list_customer'),
    path('add_enquiry/',views.add_enquiries,name='add_enquiry'),
    path('list_enquiry/',views.list_enquiry,name='list_enquiry'),
    path('add_gps/',views.add_gps_management,name='add_gps'),
    path('list_gps/',views.list_gps_management,name='list_gps'),
    path('class/',views.add_sign_class,name='class'),
    path('sign_out',views.sign_out,name='sign_out'),
    path('auto/',views.city_autocomplete,name='auto'), 
    path('insurance/',views.add_insurance,name='insurance'),
    path('path_insurance/',views.list_insurance,name='path_insurance'),
    
    # path('gps/',views.town_autocomplete,name='gps')
    
]