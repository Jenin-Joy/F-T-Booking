from django.db import models
from Guest.models import*
from Admin.models import*

# Create your models here.
class tbl_jobrequest(models.Model):
    request_date=models.DateField(auto_now_add=True)
    request_status=models.IntegerField(default=0)
    job=models.ForeignKey(tbl_job,on_delete=models.CASCADE)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    request_file=models.FileField(upload_to='Assets/Files/User')

class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=30)
    complaint_content=models.TextField()
    complaint_date=models.DateField(auto_now_add=True)
    complaint_reply=models.TextField()
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_feedback(models.Model):
    feedback_content=models.TextField()
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_tablebooking(models.Model):
    tablebokking_end=models.TimeField()
    tablebooking_date=models.DateField(auto_now_add=True)
    tablebooking_status=models.IntegerField(default=0)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    tablebooking_fordate=models.DateField()
    tablebooking_time=models.TimeField()
    tablebooking_amount = models.CharField(max_length=30)

class tbl_bookedtable(models.Model):
    table=models.ForeignKey(tbl_table,on_delete=models.CASCADE)
    tablebooking = models.ForeignKey(tbl_tablebooking, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

class tbl_booking(models.Model):
    booking_date = models.DateField(auto_now_add=True)
    booking_amount = models.CharField(max_length=30)
    booking_status = models.IntegerField(default=0)
    user = models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_cart(models.Model):
    cart_qty = models.IntegerField(default=1)
    cart_status = models.IntegerField(default=0)
    food = models.ForeignKey(tbl_food,on_delete=models.CASCADE)
    booking = models.ForeignKey(tbl_booking,on_delete=models.CASCADE)

class tbl_rating(models.Model):
    rating_review = models.CharField(max_length=30)
    rating_datetime = models.DateTimeField(auto_now_add=True)
    rating_data= models.IntegerField()
    user = models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    food = models.ForeignKey(tbl_food,on_delete=models.CASCADE)



