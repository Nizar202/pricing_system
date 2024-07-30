from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),  # مسار تسجيل الدخول
    path('', views.home, name='home'),  # المسار الرئيسي للصفحة الرئيسية
    path('create_offer/', views.create_offer, name='create_offer'),  # مسار إنشاء العرض المالي
]
