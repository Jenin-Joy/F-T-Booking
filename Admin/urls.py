from django.contrib import admin
from django.urls import path
from Admin import views
app_name='Admin'

urlpatterns = [
    path ('homepage/',views.homepage,name='homepage'),
    path ('district/',views.district,name='district'),
    path ('category/',views.category,name='category'),
    path ('adminreg/',views.adminreg,name='adminreg'),
    path ('place/',views.place,name='place'),
    path ('deleteid/<int:did>',views.deletecat,name='deletecat'),
    path ('ddis/<int:did>',views.ddis,name='ddis'),
    path ('delplace/<int:did>',views.delplace,name='delplace'),
    path ('editpalce/<int:eid>',views.editplace,name='editplace'),
    path ('editdistrict/<int:edid>',views.editdistrict,name='editdistrict'),
    path ('editcat/<int:ecid>',views.editcat,name='editcat'),
    path ('subcategory/',views.subcategory,name='subcategory'),
    path ('delsubcat/<int:did>',views.delsubcat,name='delsubcat'),
    path ('editsubcate/<int:esid>',views.editsubcate,name='editsubcate'),
    path ('supervisor/',views.supervisor,name='supervisor'),
    path ('staff/',views.staff,name='staff'),
    path ('stafftype/',views.stafftype,name='stafftype'),
    path ('food/',views.food,name='food'),
    path ('ajaxfood/',views.ajaxfood,name='ajaxfood'),
    path ('job/',views.job,name='job'),
    path ('AddTable/',views.AddTable,name='AddTable'),
    path ('AddManager/',views.AddManager,name='AddManager'),
    path ('removestaff/<int:did>',views.removestaff,name='removestaff'),
    path ('JobApplicants/<int:did>',views.JobApplicants,name='JobApplicants'),
]