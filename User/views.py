from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from User.models import *
from django.db.models import Sum
from django.http import JsonResponse
from datetime import datetime, timedelta, date
# Create your views here.
def Homepage(request):
    if "uid" in request.session:
        return render(request, 'User/Homepage.html')
    else:
        return redirect("Guest:Login")


def MyProfile(request):
    if "uid" in request.session:
        User=tbl_user.objects.get(id=request.session['uid'])
        return render(request, 'User/MyProfile.html',{'User':User})
    else:
        return redirect('Guest:Login')

def EditProfile(request):
    if "uid" in request.session:
        Edit=tbl_user.objects.get(id=request.session['uid'])
        if request.method == 'POST':
            Edit.user_name=request.POST.get('txt_name')
            Edit.user_email=request.POST.get('txt_email')
            Edit.user_contact=request.POST.get('txt_contact')
            Edit.user_address=request.POST.get('txt_address')
            Edit.save()
            return redirect("User:MyProfile")
        else:   
            return render(request, 'User/EditProfile.html',{'edit':Edit})
    else:
        return redirect("Guest:Login")


def ChangePass(request):
    if "uid" in request.session:
        Edit=tbl_user.objects.get(id=request.session['uid'])
        old=Edit.user_pass
        if request.method == 'POST':   
            oldpass=request.POST.get('txt_old') 
            newpass=request.POST.get('txt_new')
            retype=request.POST.get('txt_re')
            if oldpass==old:
                if newpass==retype:
                    Edit.user_pass=newpass
                    Edit.save() 
                    return redirect("User:MyProfile")
                else:
                    return render(request, 'User/ChangePass.html',{'msg':'Password does not match'})
        else:  
            return render(request, 'User/ChangePass.html')
    else:
        return redirect("Guest:Login")

def JobVacancy(request):
    if "uid" in request.session:
        job=tbl_job.objects.all()
        return render(request, 'User/JobVacancy.html',{'job':job})
    else:
        return redirect("Guest:Login")
    
def JobList(request,iid):
    if "uid" in request.session:
        job=tbl_job.objects.filter(id=iid)
        return render(request, 'User/JobList.html',{'job':job})
    else:
        return redirect("Guest:Login")
        
def Apply(request,jid):
    if "uid" in request.session:
        user=tbl_user.objects.get(id=request.session['uid'])
        if request.method == 'POST':
            resume=request.FILES.get('txt_resume')
            jobid=tbl_job.objects.get(id=jid)
            userid=request.session['uid']
            tbl_jobrequest.objects.create(job=jobid,user=user,request_file=resume)
            return redirect('User:JobVacancy')
        else:
            return render(request,'User/Apply.html',{'user':user})
    else:
        return redirect("Guest:Login")

def Complaint(request):
    if "uid" in request.session:
        user=tbl_user.objects.get(id=request.session['uid'])
        complaint=tbl_complaint.objects.filter(user=request.session['uid'])
        if request.method == 'POST':
            title=request.POST.get('txt_title')
            content=request.POST.get('txt_content')
            tbl_complaint.objects.create(user=user,complaint_title=title,complaint_content=content)
            return redirect('User:Complaint')
        else:
            return render(request,'User/Complaint.html',{'complaint':complaint})
    else:
        return redirect("Guest:Login")

def Menu(request):
    if "uid" in request.session:
        menu=tbl_food.objects.all()
        # if request.method == 'POST':

        # else:
        return render(request,'User/Menu.html',{'menu':menu})
    else:
        return redirect("Guest:Login")

def Feedback(request):
    if "uid" in request.session:
        user=tbl_user.objects.get(id=request.session['uid'])
        feedback=tbl_feedback.objects.filter(user=request.session['uid'])
        if request.method == 'POST':
            name=request.POST.get('txt_content')
            tbl_feedback.objects.create(user=user,feedback_content=name)
            return redirect('User:Feedback')
        else:
            return render(request,'User/Feedback.html',{'feedback':feedback})
    else:
        return redirect("Guest:Login")

def deletefeed(request,did):
    if "uid" in request.session:
        feedback=tbl_feedback.objects.get(id=did).delete()
        return redirect('User:Feedback')
    else:
        return redirect("Guest:Login")

def ViewTable(request):
    if "uid" in request.session:
        if request.method == "POST":
            seat = request.POST.getlist("txttable[]")
            time = request.POST.get("txt_time")
            day = request.POST.get("txt_date")
            if seat == [] or seat == '' or day == '':
                return render(request, "User/ViewTable.html",{"msg": "Please select a seat, date and time"})
            else:
                usercount = tbl_tablebooking.objects.filter(user=request.session["uid"],tablebooking_status=0).count()
                if usercount > 0:
                    bk = tbl_tablebooking.objects.get(user=request.session["uid"],tablebooking_status=0)
                    for i in seat:
                        tbl_bookedtable.objects.create(
                            table=tbl_table.objects.get(id=i),
                            tablebooking=tbl_tablebooking.objects.get(id=bk.id)
                        )
                    return redirect("User:Tablepayment",bk.id)
                else:
                    ti = datetime.strptime(time, "%H:%M")
                    if datetime.now() > ti:
                        return render(request, "User/ViewTable.html", {"msg": "Time already passed"})
                    else:
                        time_obj = datetime.strptime(time, "%H:%M")  # Convert string to datetime object
                        new_time = time_obj + timedelta(hours=1)
                        tb = tbooking = tbl_tablebooking.objects.create(
                            user=tbl_user.objects.get(id=request.session['uid']),
                            tablebooking_fordate = day,
                            tablebooking_time = time,
                            tablebokking_end = new_time
                        )
                        for i in seat:
                            tbl_bookedtable.objects.create(
                                table=tbl_table.objects.get(id=i),
                                tablebooking=tbl_tablebooking.objects.get(id=tb.id)
                            )
                        return redirect("User:Tablepayment",tb.id)
        return render(request,'User/ViewTable.html')
    else:
        return redirect("Guest:Login")

def Tablepayment(request, id):
    count = tbl_bookedtable.objects.filter(tablebooking=id).count()
    amount = 50 * count
    if request.method == 'POST':
        tb = tbl_tablebooking.objects.get(id=id)
        tb.tablebooking_status = 1
        tb.tablebooking_amount = amount
        tb.save()
        return redirect("User:loader")
    else:
        return render(request,'User/Payment.html',{'total':amount})

def bookchecking(request):
    min = request.GET.get("min")
    hournow = request.GET.get("hour")
    tbook = tbl_tablebooking.objects.filter(tablebooking_status=0)
    for  t in tbook:
        time = t.tablebooking_time.minute
        hour = t.tablebooking_time.hour
        if int(hournow) > hour:
            diff = (60 + int(min)) - time
        else:
            diff = int(min) - time
        if diff > 2:
            tablebooking = tbl_tablebooking.objects.get(id=t.id).delete()
    return JsonResponse({'msg':None})

def viewtablebooking(request):
    tablebook = tbl_tablebooking.objects.filter(user=request.session["uid"])
    return render(request,"User/BookedTables.html",{'tablebook':tablebook})
        
def Reservation(request,did):
    if "uid" in request.session:
        user=tbl_user.objects.get(id=request.session['uid'])
        tables=tbl_table.objects.all()
        if request.method == 'POST':
            table=tbl_table.objects.get(id=did)
            date=request.POST.get('txt_date')
            time=request.POST.get('txt_time')
            tbl_tablebooking.objects.create(user=user,table=table,tablebooking_date=date,tablebooking_time=time,tablebooking_status=1)
            return redirect('User:ViewTable')
        else:
            return render(request,'User/Reservation.html',{'tables':tables})

def Addcart(request,pid):
    if "uid" in request.session:
        food=tbl_food.objects.get(id=pid)
        User=tbl_user.objects.get(id=request.session["uid"])
        bookingcount=tbl_booking.objects.filter(user=User,booking_status=0).count()
        if bookingcount>0:
            bookingdata=tbl_booking.objects.get(user=User,booking_status=0)
            cartcount=tbl_cart.objects.filter(booking=bookingdata,food=food).count()
            if cartcount>0:
                msg="Already added"
                return render(request,"User/Menu.html",{'msg':msg})
            else:
                tbl_cart.objects.create(booking=bookingdata,food=food)
                msg="Added To cart"
                return render(request,"User/Menu.html",{'msg':msg})
        else:
            bookingdata = tbl_booking.objects.create(user=User)
            tbl_cart.objects.create(booking=tbl_booking.objects.get(id=bookingdata.id),food=food)
            msg="Added To cart"
            return render(request,"User/Menu.html",{'msg':msg})
    else:
        return redirect("Guest:Login")

def MyCart(request):
    if "uid" in request.session:
        if request.method=="POST":
            bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
            bookingdata.booking_amount=request.POST.get("carttotalamt")
            bookingdata.booking_status=1
            bookingdata.save()
            cart = tbl_cart.objects.filter(booking=bookingdata)
            for i in cart:
                i.cart_status = 1
                i.save()
            return redirect("User:productpayment")
        else:
            bookcount = tbl_booking.objects.filter(user=request.session["uid"],booking_status=0).count()
            if bookcount > 0:
                book = tbl_booking.objects.get(user=request.session["uid"],booking_status=0)
                request.session["bookingid"] = book.id
                cart = tbl_cart.objects.filter(booking=book)
                for i in cart:
                    total_cart = tbl_cart.objects.filter(food=i.food.id, cart_status=1).aggregate(total=Sum('cart_qty'))['total']
                    # print(total_stock)
                    # print(total_cart)
                
                    if total_cart is None:
                        total_cart = 0
                    total =   total_cart
                    # i.total_stock = total
                return render(request,"User/MyCart.html",{'cartdata':cart})
            else:
                return render(request,"User/MyCart.html")
    else:
        return redirect("Guest:Login")
   
        

def DelCart(request,did):
    if "uid" in request.session:
        tbl_cart.objects.get(id=did).delete()
        return redirect("User:Mycart")
    else:
        return redirect("Guest:Login")

def CartQty(request):
    if "uid" in request.session:
        qty=request.GET.get('QTY')
        cartid=request.GET.get('ALT')
        cartdata=tbl_cart.objects.get(id=cartid)
        cartdata.cart_qty=qty
        cartdata.save()
        return redirect("User:Mycart")  
    else:
        return redirect("Guest:Login") 

def payment(request,id):
    if "uid" in request.session:
        booking = tbl_booking.objects.get(id=id)
        food = tbl_food.objects.get(id=booking.food.id)
        amount = food.food_price
        if request.method == "POST":
            booking.booking_status = 2
            booking.save()
            return redirect("User:loader")
        else:
            return render(request,"User/Payment.html", {"total":amount})
    else:
        return redirect("Guest:Login")

def loader(request):
    if "uid" in request.session:
        return render(request,"User/Loader.html")
    else:
        return redirect("Guest:Login")

def paymentsuc(request):
    if "uid" in request.session:
        return render(request,"User/Payment_suc.html")
    else:
        return redirect("Guest:Login")

def productpayment(request): 
    if "uid" in request.session:
        bookingdata = tbl_booking.objects.get(id=request.session["bookingid"])
        amt = bookingdata.booking_amount
        if request.method == "POST":
            bookingdata.booking_status = 2
            bookingdata.save()
            return redirect("User:loader")
        else:
            return render(request,"User/Payment.html",{"total":amt})
    else:
        return redirect("Guest:Login")

def OrderAmount(request):
    if "uid" in request.session:
        booking = tbl_booking.objects.filter(user=request.session['uid'], booking_status__gte=2)
        return render(request,"User/OrderAmount.html",{'booking':booking})
    else:
        return redirect("Guest:Login")

def MyOrders(request,id):
    if "uid" in request.session:
        order=tbl_cart.objects.filter(booking=id)
        return render(request,"User/MyOrders.html",{"order":order})
    else:
        return redirect("Guest:Login")

def Rating(request):
    if "uid" in request.session:
        return render(request,"User/Rating.html")
    else:
        return redirect("Guest:Login")

def ajaxgettable(request):
    if request.GET.get("date") != "" and request.GET.get("time") != "":
        dates = request.GET.get("date")
        time = request.GET.get("time")
        date_obj = datetime.strptime(dates, "%Y-%m-%d").date()
        time_obj = datetime.strptime(time, "%H:%M").time()  # Converts "17:00" to time object
        time_str = f"{time_obj.hour:02d}:{time_obj.minute:02d}"
        tables = tbl_table.objects.all()
        return render(request,"User/AjaxGetTable.html",{"table":tables,"date":date_obj, "time":time_str})
    elif request.GET.get("date") != "":
        dates = request.GET.get("date")
        date_obj = datetime.strptime(dates, "%Y-%m-%d").date()
        time = datetime.now().strftime("%H:%M")
        tables = tbl_table.objects.all()
        return render(request,"User/AjaxGetTable.html",{"table":tables,"date":date_obj, "time":time.hour})
    elif request.GET.get("time")!= "":
        dates = date.today()
        time = request.GET.get("time")
        time_obj = datetime.strptime(time, "%H:%M").time()  # Converts "17:00" to time object
        time_str = f"{time_obj.hour:02d}:{time_obj.minute:02d}"
        tables = tbl_table.objects.all()
        return render(request,"User/AjaxGetTable.html",{"table":tables,"date":dates, "time":time_str})
    else:
        dates = date.today()
        time = datetime.now().strftime("%H:%M")
        tables = tbl_table.objects.all()
        return render(request,"User/AjaxGetTable.html",{"table":tables,"date":dates, "time":time})

def ajaxgettablecount(request):
    table = tbl_table.objects.get(id=request.GET.get("table"))
    return JsonResponse({"count":table.table_count})

def Head(request):
    # if "uid" in request.session:
    return render(request,"User/Head.html")

def Foot(request):
    return render(request,"User/Foot.html")