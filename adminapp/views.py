from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponse
# Create your views here.


def index(request):
    return render(request,'basic/index.html')

def register(request):
    return render(request,'basic/register.html')    

def login(request):
    return render(request,'basic/login.html')  

def admin_index(request):
    context={}
    try:
        get_admin=cred.objects.get(username=request.session["admin"])
        context['admin']=get_admin
    except:
        easygui.msgbox("verification failed",title="failed")
        return redirect('cred:login')       
    return render(request,'admin/admin_index.html')       

def view_requests(request):
    context={}
    try:
        get_admin=cred.objects.get(username=request.session["admin"])
        context['admin']=get_admin
    except:
        easygui.msgbox("verification failed",title="failed")
        return redirect('cred:login')
        get_new_req=cred.objects.values('username').filter(u_status=0)
        user_det=user_det.objects.filter(username__in=get_new_req)

        contest['new_request']=user_det       
    return render(request,'admin/viewrequests.html',context)


def approve(request):
    context={}
    st=request.GET['st']
    try:
        get_admin=cred.objects.get(username=request.session["admin"])
        context['admin']=get_admin
    except:
        easygui.msgbox("verification failed",title="failed")
        return redirect('cred:login')
    
    try:
        get_user=cred.objects.get(username=st)
        get_user.u_status=1
        get_user.save()
    except:
        easygui.msgbox("invalid user details",title="failed")      
    return redirect('cred:view_requests')

def add_catagory(request):
    if request.method=="POST":
        title=request.POST.get('title')
        add_catagory=catagory(title=title)
        add_catagory.save()
        easygui.msgbox("new catagory added",title="success")
return render(request,"admin/add_catagory.html")

def add_subcatagory(request):
    context={}
    try:
        get_admin=cred.objects.get(username=request.session["admin"])
        context['admin']=get_admin
    except:
        easygui.msgbox("verification failed",title="failed")
        return redirect('cred:login')
    if request.method=="POST":
        title=request.POST.get('title')    
        cat=request.POST.get('cat')
        add_catagory=subcatagory(title=title,cat_id=cat)
        add_catagory.save()
        easygui.msgbox("new subcatagory added",title="success")
    context['catlist']=catagory.objects.filter()
    print(context['catlist'])
    return render(request,'admin/add_subcatagory.html',context)

def add_product(request):
    context={}
    try:
        get_admin=cred.objects.get(username=request.session["admin"])
        context['admin']=get_admin
    except:
        easygui.msgbox("verification failed",title="failed")
        return redirect('cred:login')
    if request.method=="POST":
        title=request.POST.get('title')
        price=request.POST.get('price') 
        photo=request.POST.get('photo')    
        cat=request.POST.get('cat')
        sub_cat=request.POST.get('subcat')

