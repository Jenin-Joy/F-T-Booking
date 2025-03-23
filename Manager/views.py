from django.shortcuts import render,redirect
from Admin.models import*
from Guest.models import*
from Manager.models import*
from User.models import*

# Create your views here.
def Staff(request):
    if "mid" in request.session:
        staff=tbl_staff.objects.all()
        return render(request,'Manager/Staff.html',{'staff':staff})
    else:
        return redirect("Guest:Login")


def Schedule(request,sid):
    if "mid" in request.session:
        schedule=tbl_schedule.objects.filter(staff=sid)
        if request.method=='POST':
            date=request.POST.get('txt_date')
            fromtime=request.POST.get('txt_frmtime')
            totime=request.POST.get('txt_totime')
            work=request.POST.get('txt_work')
            staffid=tbl_staff.objects.get(id=sid)
            tbl_schedule.objects.create(schedule_todate=date,schedule_fromtime=fromtime,schedule_totime=totime,schedule_work=work,staff=staffid)
            return render(request,'Manager/Schedule.html',{'schedule':schedule})
        else:
            return render(request,'Manager/Schedule.html',{'schedule':schedule})
    else:
        return redirect("Guest:Login")

def WorkedHours(request,wid):
    if "mid" in request.session:
        edit=tbl_schedule.objects.get(id=wid)
        if request.method=='POST':  
            edit.Schedule_work_fromtime=request.POST.get('txt_frmtime')
            edit.Schedule_work_totime=request.POST.get('txt_totime')
            edit.save()
            return render(request,'Manager/WorkedHours.html')
        else:
            return render(request,'Manager/WorkedHours.html')
    else:
        return redirect("Guest:Login")


def homepage(request):
    if "mid" in request.session:
        return render(request, 'Manager/Homepage.html')
    else:
        return redirect("Guest:Login")

def MyProfile(request):
    if "mid" in request.session:
        Manager=tbl_manager.objects.get(id=request.session['mid'])
        return render(request, 'Manager/MyProfile.html',{'Manager':Manager})
    else:
        return redirect("Guest:Login")


def EditProfile(request):
    if "mid" in request.session:
        Edit=tbl_manager.objects.get(id=request.session['mid'])
        if request.method == 'POST':
            Edit.manager_name=request.POST.get('txt_name')
            Edit.manager_email=request.POST.get('txt_email')
            Edit.manager_contact=request.POST.get('txt_contact')
            Edit.save()
            return redirect("Manager:MyProfile")
        else:   
            return render(request, 'Manager/EditProfile.html',{'edit':Edit})
    else:
        return redirect("Guest:Login")


def ChangePass(request):
    if "mid" in request.session:
        Edit=tbl_manager.objects.get(id=request.session['mid'])
        old=Edit.manager_password
        if request.method == 'POST':   
            oldpass=request.POST.get('txt_old') 
            newpass=request.POST.get('txt_new')
            retype=request.POST.get('txt_re')
            if oldpass==old:
                if newpass==retype:
                    Edit.manager_password=newpass
                    Edit.save() 
                    return redirect("Manager:MyProfile")
                else:
                    return render(request, 'Manager/ChangePass.html',{'msg':'Password does not match'})
        else:  
            return render(request, 'Manager/ChangePass.html')
    else:
        return redirect("Guest:Login")


def Orders(request):
    if "mid" in request.session:
        # orders=tbl_cart.objects.filter(cart_status=1,booking__booking_status=2)
        orders = tbl_cart.objects.filter(cart_status=1, booking__booking_status__gte=2)#greater than or equal to 2.
        return render(request, 'Manager/Orders.html',{'order':orders})
    else:
        return redirect("Guest:Login")


def pick(request,id):
    if "mid" in request.session:
        order=tbl_booking.objects.get(id=id)
        order.booking_status=3
        order.save()
        return render(request, 'Manager/Orders.html',{'msg':"Updated"})
    else:
        return redirect("Guest:Login")


def done(request,did):
    if "mid" in request.session:
        done=tbl_booking.objects.get(id=did)
        done.booking_status=4
        done.save()
        return render(request, 'Manager/Orders.html',{'msg2':"Completed"})
    else:
        return redirect("Guest:Login")


def TableReservation(request):
    if "mid" in request.session:
        table=tbl_tablebooking.objects.all()
        return render(request, 'Manager/TableReservation.html',{'table':table})
    else:
        return redirect("Guest:Login")