from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('cart',views.show_cart,name='cart'),
    path('add_tocart',views.add_tocart,name='add_tocart'),
    path('remove_item/<pk>',views.remove_item,name='remove_item'),
    path('checkout',views.checkout,name='checkout'),
    path('orders',views.show_orders,name='orders'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)