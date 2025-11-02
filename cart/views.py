from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import CartItem

def cart_view(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id not in cart:
        cart.append(product_id)
    request.session['cart'] = cart
    return redirect('cart:cart_view')

def cart_view(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)
    return render(request, 'cart/cart_view.html', {'products': products})


def remove_from_cart(request, product_id):
    """
    Remove a product from the user's cart.
    """
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.filter(user=request.user, product=product).first()
    if cart_item:
        cart_item.delete()
    return redirect('cart:cart_view')


def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart/cart_view.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1  # increase quantity if already in cart
    cart_item.save()

    return redirect('cart:cart_view')