from django.contrib import admin
from django.urls import path
from Manager import views
app_name='Manager'

urlpatterns = [
     path ('homepage/',views.homepage,name='homepage'),
     path('MyProfile/', views.MyProfile,name='MyProfile'),
     path('EditProfile/', views.EditProfile, name='EditProfile'),
     path('ChangePass/', views.ChangePass, name='ChangePass'),
     path ('Staff/',views.Staff,name='Staff'),
     path ('Schedule/<int:sid>',views.Schedule,name='Schedule'),
     path ('WorkedHours/<int:wid>',views.WorkedHours,name='WorkedHours'),
     path ('Orders/',views.Orders,name='Orders'),
     path ('pick/<int:id>',views.pick,name='pick'),
     path ('done/<int:did>',views.done,name='done'),
     path ('TableReservation/',views.TableReservation,name='TableReservation'),
]