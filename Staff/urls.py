from django.contrib import admin
from django.urls import path
from Staff import views
app_name='Staff'

urlpatterns = [
    path('Homepage/', views.Homepage,name='Homepage'),
    # path('Schedule/',views.Schedule,name='Schedule'),
]