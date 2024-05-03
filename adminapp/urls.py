from django.urls import path
from . import views

app_name='cred'

urlpatterns=[
    path("",views.index,name='index'),
    path("index",views.index,name='index'),
    path("register",views.register,name='register'),
    path("login",views.login,name='login'), 
    path("admin_index",views.admin_index,name='admin_index'),
    path("viewrequests",views.view_requests,name='viewrequests'),
    path("add_catagory",views.add_catagory,name='add_catagory'),
    path("approve",views.approve,name='approve'),
    path("add_subcatagory",views.add_subcatagory,name='add_subcatagory'),
    path("add_product",views.add_product,name='add_products'),
    path("get_subcat",views.get_subcat,name='get_subcat'),
]
