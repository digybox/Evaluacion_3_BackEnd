from django.contrib import admin
from django.urls import path, include

urlpatterns = [
<<<<<<< HEAD
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # login/logout
    path("", include("app.urls")),
=======
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
>>>>>>> 948abcf8f54b812fa17f640d3add663291a2c337
]
