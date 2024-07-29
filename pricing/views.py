# views.py
from django.shortcuts import render, redirect
from pricing_system.forms import CustomerForm, ProductForm, OfferForm
from .models import Customer, Product, Offer

def home(request):
    return render(request, 'pricing/home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'pricing/product_list.html', {'products': products})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'pricing/create_product.html', {'form': form})

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerForm()
    return render(request, 'pricing/create_customer.html', {'form': form})

def create_offer(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = OfferForm()
    return render(request, 'pricing/create_offer.html', {'form': form})
