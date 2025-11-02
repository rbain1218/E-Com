from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product


@login_required
def become_seller(request):
    """
    When a normal user clicks 'Become a Seller',
    we mark them as a seller and redirect to the seller dashboard.
    """
    user = request.user
    user.is_seller = True  # Assuming your User model has this boolean field
    user.save()
    messages.success(request, "You are now registered as a Seller! 🎉")
    return redirect('seller:seller_dashboard')  # ✅ fixed namespace


@login_required
def seller_dashboard(request):
    """
    Seller dashboard showing all products added by the logged-in seller.
    """
    if not request.user.is_seller:
        messages.error(request, "You must be a seller to access this page.")
        return redirect('/')

    # Get all products uploaded by this seller
    products = Product.objects.filter(seller=request.user)

    return render(request, 'seller/dashboard.html', {
        'products': products
    })


@login_required
def add_product(request):
    """
    Form for sellers to add new products to the website.
    """
    if not request.user.is_seller:
        messages.error(request, "Only sellers can add products.")
        return redirect('/')

    if request.method == "POST":
        name = request.POST.get("name")
        category = request.POST.get("category")
        price = request.POST.get("price")
        grade = request.POST.get("grade")
        description = request.POST.get("description")
        image = request.FILES.get("image")

        # Create the product
        Product.objects.create(
            name=name,
            category=category,
            price=price,
            grade=grade,
            description=description,
            image=image,
            seller=request.user
        )
        messages.success(request, f"✅ Product '{name}' added successfully!")
        return redirect('seller:seller_dashboard')  # ✅ fixed namespace

    return render(request, 'seller/add_product.html')


@login_required
def delete_product(request, product_id):
    """
    Allow a seller to delete their own product.
    """
    try:
        product = Product.objects.get(id=product_id, seller=request.user)
        product.delete()
        messages.success(request, "🗑️ Product deleted successfully.")
    except Product.DoesNotExist:
        messages.error(request, "Product not found or you don’t have permission.")
    return redirect('seller:seller_dashboard')  # ✅ fixed namespace
