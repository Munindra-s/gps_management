from django.urls import path
from . import views
urlpatterns =[
    path('customer',views.custmas,name='customer'),  
    path('list_customer/',views.list_customer,name='list_customer'),
    path('add_gps/',views.add_gps_management,name='add_gps'),
    path('list_gps/',views.list_gps_management,name='list_gps'),
]    