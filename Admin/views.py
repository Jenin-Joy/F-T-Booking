from django.shortcuts import render,redirect
from Admin.models import* # import table data of Admin app
from datetime import date
from User.models import*
# Create your views here.


def district(request):
    if "aid" in request.session:
        district=tbl_district.objects.all()#select/display avan
        if request.method == 'POST':# database lek value insert cheyyan
            name=request.POST.get('txt_district')#input type le name
            tbl_district.objects.create(district_name=name)# table field name
            return render(request, 'Admin/District.html',{'dis':district})
        else:
            return render(request, 'Admin/District.html',{'dis':district})#refresh automatically
    else:
        return redirect("Guest:Login")


def category(request):
    if "aid" in request.session:
        category=tbl_category.objects.all()
        if request.method == 'POST':
            name=request.POST.get('txt_cate')#input type le name
            tbl_category.objects.create(category_name=name)# table field name
            return render(request, 'Admin/Category.html',{'cat':category})  
        else:
            return render(request, 'Admin/Category.html',{'cat':category})
    else:
        return redirect("Guest:Login")

        
def adminreg(request):
    if "aid" in request.session:
        if request.method == 'POST':
            name=request.POST.get('txt_name')
            email=request.POST.get('txt_email')
            password=request.POST.get('txt_pass')
            tbl_adminreg.objects.create(admin_name=name, admin_email=email,admin_password=password)
        return render(request, 'Admin/AdminReg.html')
    else:
        return redirect("Guest:Login")


def place(request):
    if "aid" in request.session:
        place=tbl_place.objects.all()
        district=tbl_district.objects.all()
        if request.method == 'POST':
            # print(request.POST.get('sel_district'))
            dist=tbl_district.objects.get(id=request.POST.get('sel_district'))
            plac=request.POST.get('txt_place')
            tbl_place.objects.create(place_name=plac,district=dist)
            return render(request, 'Admin/Place.html',{'msg':"Data Inserted"})
            # return redirect('Admin:place')
            # return render(request, 'Admin/Place.html',{'dis':district,'plc':place})
        else:
            return render(request, 'Admin/Place.html',{'dis':district,'plc':place})
    else:
        return redirect("Guest:Login")


def deletecat(request,did):
    if "aid" in request.session:
        tbl_category.objects.get(id=did).delete()
        return redirect('Admin:category')
    else:
        return redirect("Guest:Login")

def ddis(request,did):
    if "aid" in request.session:
        tbl_district.objects.get(id=did).delete()
        return redirect('Admin:district')
    else:
        return redirect("Guest:Login")

def delplace(request,did):
    if "aid" in request.session:
        tbl_place.objects.get(id=did).delete()
        return redirect('Admin:place')
    else:
        return redirect("Guest:Login")

def editplace(request,eid):
    if "aid" in request.session:
        district=tbl_district.objects.all()
        edit=tbl_place.objects.get(id=eid)
        if request.method == 'POST':
            name=request.POST.get('txt_place')
            dis=tbl_district.objects.get(id=request.POST.get('sel_district'))
            edit.district=dis
            edit.place_name=name
            edit.save()
            return redirect('Admin:place')
        else:
            return render(request,'Admin/Place.html',{'editplace':edit,'dis':district})
    else:
        return redirect("Guest:Login")


def editdistrict(request,edid):
    if "aid" in request.session:
        edit=tbl_district.objects.get(id=edid)
        if request.method == 'POST':
            edit.district_name=request.POST.get('txt_district')
            edit.save()
            return redirect('Admin:district')
        else:
            return render(request,'Admin/District.html',{'data':edit})
    else:
        return redirect("Guest:Login")


def editcat(request,ecid):
    if "aid" in request.session:
        edit=tbl_category.objects.get(id=ecid)
        if request.method =='POST':
            edit.category_name=request.POST.get('txt_cate')
            edit.save()
            return redirect('Admin:category')
        else:
            return render(request,'Admin/Category.html',{'data':edit})
    else:
        return redirect("Guest:Login")


def subcategory(request):
    if "aid" in request.session:
        category=tbl_category.objects.all()
        subcategory=tbl_subcategory.objects.all()
        if request.method == 'POST':
            sub=request.POST.get('txt_subcategory')
            cate=tbl_category.objects.get(id=request.POST.get('sel_category'))
            tbl_subcategory.objects.create(subcategory_name=sub,category=cate)
            return render(request, 'Admin/SubCategory.html',{'msg':"Data Inserted"}) 
        else:
            return render(request,'Admin/SubCategory.html',{'categ':category,'subcat':subcategory})
    else:
        return redirect("Guest:Login")

def delsubcat(request,did):
    if "aid" in request.session:
        tbl_subcategory.objects.get(id=did).delete()
        return redirect('Admin:subcategory')
    else:
        return redirect("Guest:Login")


def editsubcate(request,esid):
    if "aid" in request.session:
        category=tbl_category.objects.all()
        edit=tbl_subcategory.objects.get(id=esid)
        if request.method =='POST':
            edit.subcategory_name=request.POST.get('txt_subcategory')
            edit. cate=tbl_category.objects.get(id=request.POST.get('sel_category'))
            edit.save()
            return redirect('Admin:subcategory')
        else:
            return render(request,'Admin/SubCategory.html',{'data':edit,'categ':category})
    else:
        return redirect("Guest:Login")

def supervisor(request):
    if "aid" in request.session:
        supervisor=tbl_supervisor.objects.all()
        if request.method == 'POST':
            name=request.POST.get('txt_name')
            email=request.POST.get('txt_email')
            address=request.POST.get('txt_address')
            contact=request.POST.get('txt_contact')
            photo=request.FILES.get('txt_photo')
            password=request.POST.get('txt_password')
            tbl_supervisor.objects.create(supervisor_name=name,supervisor_email=email,supervisor_address=address,supervisor_contact=contact,supervisor_photo=photo,supervisor_password=password)
            return render(request, 'Admin/Supervisor.html',{'sup':supervisor})
        else:
            return render(request, 'Admin/Supervisor.html',{'sup':supervisor})
    else:
        return redirect("Guest:Login")

            
def staff(request):
    if "aid" in request.session:
        staff=tbl_staff.objects.all()
        sttype=tbl_stafftype.objects.all()
        if request.method == 'POST':
            name=request.POST.get('txt_name')
            email=request.POST.get('txt_email')
            sstype=tbl_stafftype.objects.get(id=request.POST.get('sel_stafftype'))
            contact=request.POST.get('txt_contact')
            photo=request.FILES.get('txt_photo')
            password=request.POST.get('txt_password')
            tbl_staff.objects.create(staff_name=name,staff_email=email,staff_contact=contact,staff_photo=photo,staff_password=password,stype=sstype)
            return render(request, 'Admin/Staff.html',{'staff':staff,'typestaff':sttype})
        else:
            return render(request, 'Admin/Staff.html',{'staff':staff,'typestaff':sttype})
    else:
        return redirect("Guest:Login")

def removestaff(request,did):
    if "aid" in request.session:
        tbl_staff.objects.get(id=did).delete()
        return redirect('Admin:staff')
    else:
        return redirect("Guest:Login")

def stafftype(request):
    if "aid" in request.session:
        stafftype=tbl_stafftype.objects.all()
        if request.method == 'POST':
            name=request.POST.get('txt_stafftype')
            tbl_stafftype.objects.create(stafftype_name=name)
            return redirect('Admin:stafftype')
        else:
            return render(request, 'Admin/StaffType.html',{'stafftype':stafftype})
    else:
        return redirect("Guest:Login")

def homepage(request):
    if "aid" in request.session:
        return render(request, 'Admin/Homepage.html')
    else:
        return redirect("Guest:Login")
    

def food(request):
    if "aid" in request.session:
        cat=tbl_category.objects.all()
        food=tbl_food.objects.all()
        if request.method == 'POST':
            name=request.POST.get('txt_name')
            details=request.POST.get('txt_details')
            price=request.POST.get('txt_price')
            subcategory=tbl_subcategory.objects.get(id=request.POST.get('sel_subcategory'))
            photo=request.FILES.get('txt_photo')
            tbl_food.objects.create(food_name=name,food_price=price,food_details=details,food_photo=photo,subcategory=subcategory)
        return render(request, 'Admin/Food.html',{'cat':cat})
    else:
        return redirect("Guest:Login")

def ajaxfood(request):
    if "aid" in request.session:
        category = tbl_category.objects.get(id=request.GET.get("did"))   
        sub = tbl_subcategory.objects.filter(category=category)
        return render(request,"Admin/Ajaxfood.html",{"food":sub})
    else:
        return redirect("Guest:Login")


def job(request):
    if "aid" in request.session:
        job=tbl_job.objects.all()
        if request.method == 'POST':
            name=request.POST.get('txt_name')
            details=request.POST.get('txt_details')
            vdate=request.POST.get('txt_date')
            hours=request.POST.get('txt_hours')
            salary=request.POST.get('txt_salary')
            tbl_job.objects.create(job_name=name,job_details=details,job_validdate=vdate,job_salary=salary,job_hours=hours)
            return redirect('Admin:job')
        else:
            return render(request, 'Admin/Job.html',{'job':job})
    else:
        return redirect("Guest:Login")

def AddTable(request):
    if "aid" in request.session:
        table=tbl_table.objects.all()
        if request.method == 'POST':
            number=request.POST.get('num_table')
            seat=request.POST.get('num_seat')
            tbl_table.objects.create(table_number=number,table_count=seat)
            return redirect('Admin:AddTable')
        else:
            return render(request, 'Admin/AddTable.html',{'table':table})
    else:
        return redirect("Guest:Login")


def AddManager(request):
    if "aid" in request.session:
        manager=tbl_manager.objects.all()
        if request.method == 'POST':
            name=request.POST.get('txt_name')
            email=request.POST.get('txt_email')
            password=request.POST.get('txt_pass')
            photo=request.FILES.get('txt_photo')
            contact=request.POST.get('txt_contact')
            tbl_manager.objects.create(manager_name=name,manager_email=email,manager_password=password,manager_photo=photo,manager_contact=contact)
            return redirect('Admin:AddManager')
        else:
            return render(request, 'Admin/AddManager.html',{'manager':manager})
    else:
        return redirect("Guest:Login")

def JobApplicants(request,did):
    if "aid" in request.session:
        job=tbl_jobrequest.objects.filter(job=did)
        return render(request, 'Admin/JobApplicants.html',{'job':job,})
    else:
        return redirect("Guest:Login")
