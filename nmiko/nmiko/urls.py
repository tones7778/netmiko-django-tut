from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('netinfo/', include('netinfo.urls')),
    path('admin/', admin.site.urls),
]
