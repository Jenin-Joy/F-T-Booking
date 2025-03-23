from django.db import models


# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=30)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=30)

class tbl_adminreg(models.Model):
    admin_name=models.CharField(max_length=30)
    admin_password=models.CharField(max_length=30)
    admin_email=models.CharField(max_length=30)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=30)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=30)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)

class tbl_supervisor(models.Model):
    supervisor_name=models.CharField(max_length=30)
    supervisor_contact=models.CharField(max_length=30)
    supervisor_address=models.CharField(max_length=30)
    supervisor_email=models.CharField(max_length=30)
    supervisor_password=models.CharField(max_length=30)
    supervisor_status=models.CharField(max_length=30)
    supervisor_photo=models.FileField(upload_to='Assets/Files/User')

class tbl_stafftype(models.Model):
    stafftype_name=models.CharField(max_length=30)

class tbl_staff(models.Model):
    staff_name=models.CharField(max_length=30)
    staff_contact=models.CharField(max_length=30)
    staff_email=models.CharField(max_length=30)
    staff_password=models.CharField(max_length=30)
    staff_status=models.CharField(max_length=30)
    staff_photo=models.FileField(upload_to='Assets/Files/User')
    stype=models.ForeignKey(tbl_stafftype,on_delete=models.CASCADE)
    staff_experience=models.IntegerField()

class tbl_food(models.Model):
    food_name=models.CharField(max_length=30)
    food_details=models.CharField(max_length=330)
    food_price=models.CharField(max_length=30)
    food_photo=models.FileField(upload_to='Assets/Files/Food')
    food_status=models.CharField(max_length=30)
    subcategory=models.ForeignKey(tbl_subcategory,on_delete=models.CASCADE)

class tbl_job(models.Model):
    job_name=models.CharField(max_length=30)
    job_details=models.CharField(max_length=130)
    job_status=models.CharField(max_length=40)
    job_postdate=models.DateField(auto_now_add=True)
    job_validdate=models.DateField(max_length=30)
    job_hours=models.CharField(max_length=30)
    job_salary=models.CharField(max_length=30)

class tbl_table(models.Model):
    table_number=models.IntegerField()
    table_count=models.IntegerField()

class tbl_manager(models.Model):
    manager_name=models.CharField(max_length=30)
    manager_email=models.CharField(max_length=30)
    manager_contact=models.IntegerField()
    manager_password=models.CharField(max_length=30)
    manager_photo=models.FileField(upload_to='Assets/Files/Manager')