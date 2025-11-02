from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Q
from django.shortcuts import render
from .models import Product
def home(request):
    # Extract unique categories from Product table instead of Category model
    categories = Product.objects.values_list('category', flat=True).distinct()
    products = Product.objects.all()
    return render(request, 'products/home.html', {'categories': categories, 'products': products})


def home(request):
    products = Product.objects.all()
    return render(request, 'products/home.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})