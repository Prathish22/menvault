from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('cart',views.show_cart,name='cart'),
    path('add_tocart',views.add_tocart,name='add_tocart')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)