# urls.py
from django.urls import path
from pricing import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/new/', views.create_product, name='create_product'),
    path('customers/new/', views.create_customer, name='create_customer'),
    path('offers/new/', views.create_offer, name='create_offer'),
]
