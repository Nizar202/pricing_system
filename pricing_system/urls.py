# pricing_system/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pricing.urls')),  # تأكد من أن هذا المسار يوجه إلى ملف URLs في التطبيق الخاص بك
]
