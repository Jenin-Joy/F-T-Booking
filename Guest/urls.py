from django.contrib import admin
from django.urls import path
from Guest import views
app_name='Guest'

urlpatterns = [
     path ('Registration/',views.Registration,name='Registration'),
     path ('ajaxplace/',views.ajaxplace,name='ajaxplace'),
     path ('Login/', views.Login,name='Login'),
     path ('',views.Index,name='Index'),
     ]