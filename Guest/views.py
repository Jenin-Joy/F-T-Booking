from django.shortcuts import render,redirect
from Admin.models import*
from Guest.models import*


# Create your views here.
def Registration(request):
    district=tbl_district.objects.all()
    if request.method == 'POST':    
        name=request.POST.get('txt_name')
        pla=tbl_place.objects.get(id=request.POST.get('selplace'))
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_number')
        address=request.POST.get('txt_address')
        password=request.POST.get('txt_pass')
        photo=request.FILES.get('txt_photo')
        tbl_user.objects.create(user_name=name,user_contact=contact,user_address=address,user_pass=password,user_email=email,user_photo=photo,place=pla)
    return render(request,'Guest/Registration.html',{'dis':district})

def ajaxplace(request):
    district = tbl_district.objects.get(id=request.GET.get("did"))   
    Place = tbl_place.objects.filter(district=district)
    return render(request,"Guest/AjaxPlace.html",{"place":Place})

def Login(request):
    if request.method == 'POST':
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_pass')

        usercount=tbl_user.objects.filter(user_email=email,user_pass=password).count()
        admincount=tbl_adminreg.objects.filter(admin_email=email,admin_password=password).count()
        managercount=tbl_manager.objects.filter(manager_email=email,manager_password=password).count()

        if usercount > 0:
            user=tbl_user.objects.get(user_email=email,user_pass=password)
            request.session['uid']=user.id
            return redirect("User:Homepage")
        elif admincount > 0:
            admin=tbl_adminreg.objects.get(admin_email=email,admin_password=password)
            request.session['aid']=admin.id
            return redirect("Admin:homepage")
        elif managercount > 0:
            manager=tbl_manager.objects.get(manager_email=email,manager_password=password)
            request.session['mid']=manager.id
            return redirect("Manager:homepage")
        elif staffcount > 0:
            staff=tbl_staff.objects.get(staff_email=email,staff_password=password)
            request.session['sid']=staff.id
            return redirect("Staff:Homepage")
        else:
            return render(request,"Guest/Login.html",{'msg':"Invalid Data"})
    else:
        return render(request,"Guest/Login.html")

def Index(request):
    return render(request,"Guest/Index.html")