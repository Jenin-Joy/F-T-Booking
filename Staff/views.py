from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from User.models import *
# Create your views here.


def Homepage(request):
    if "sid" in request.session:
        return render(request, 'Staff/Homepage.html')
    else:
        return redirect("Guest:Login")


