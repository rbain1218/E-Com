from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
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
