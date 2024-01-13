# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("studentsapp.urls")),
    path("api/", include("usersApp.urls")),
    path('users/', include('django.contrib.auth.urls'))
    # Add other URLs as needed
]
