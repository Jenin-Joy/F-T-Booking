from django.db import models
from Admin.models import*

# Create your models here.
class tbl_schedule(models.Model):
    schedule_date=models.DateField(auto_now_add=True)
    schedule_todate=models.DateField(max_length=30)
    schedule_fromtime=models.CharField(max_length=30)
    schedule_totime=models.CharField(max_length=30)
    staff=models.ForeignKey(tbl_staff,on_delete=models.CASCADE)
    schedule_work=models.CharField(max_length=50)
    Schedule_work_fromtime=models.CharField(max_length=30)
    Schedule_work_totime=models.CharField(max_length=30)