from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User
from products.models import Product
from cart.models import CartItem

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    users = User.objects.all()
    products = Product.objects.all()
    cart_items = CartItem.objects.all()

    context = {
        'users': users,
        'products': products,
        'cart_items': cart_items,
    }
    return render(request, 'dashboard/admin_dashboard.html', context)


# ===== PRODUCT MANAGEMENT =====
@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        Product.objects.create(name=name, price=price, description=description, image=image)
        return redirect('dashboard:admin_dashboard')
    return render(request, 'dashboard/add_product.html')


@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        if request.FILES.get('image'):
            product.image = request.FILES.get('image')
        product.save()
        return redirect('dashboard:admin_dashboard')
    return render(request, 'dashboard/edit_product.html', {'product': product})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('dashboard:admin_dashboard')


# ===== USER MANAGEMENT =====
@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if not user.is_superuser:  # prevent deleting admin
        user.delete()
    return redirect('dashboard:admin_dashboard')
