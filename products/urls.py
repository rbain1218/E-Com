from django.urls import path
from .views import home
from . import views 

app_name = 'products'
urlpatterns = [
    path('', home, name='home'),
        path('product/<int:pk>/', views.product_detail, name='product_detail'),

]
