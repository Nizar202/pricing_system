from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pricing.urls')),  # تضمين مسارات تطبيق pricing
    path('login/', include('django.contrib.auth.urls')),  # مسارات تسجيل الدخول الافتراضية
]
