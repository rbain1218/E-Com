from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('products.urls', 'products'), namespace='products')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('seller/', include(('seller.urls', 'seller'), namespace='seller')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('chat/', include(('chat.urls', 'chat'), namespace='chat')),
    path('dashboard/', include(('dashboard.urls', 'dashboard'), namespace='dashboard')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
