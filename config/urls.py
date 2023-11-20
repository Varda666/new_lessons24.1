from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('lms_service.urls', 'lms_service'), namespace='lms_service')),
    path('users/', include(('users.urls', 'users'), namespace='users'))
    ]

