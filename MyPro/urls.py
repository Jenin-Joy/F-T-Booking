
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('Admin/',include('Admin.urls')),
    path('',include('Guest.urls')),
    path('User/',include('User.urls')),
    path('Manager/',include('Manager.urls')),
    path('Staff/',include('Staff.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)