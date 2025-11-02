from django.urls import path
from . import views

app_name = 'seller' 

urlpatterns = [
    path('become/', views.become_seller, name='become_seller'),
    path('dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('add/', views.add_product, name='add_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
