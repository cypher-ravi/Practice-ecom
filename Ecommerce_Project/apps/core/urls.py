from django.urls import path,include
from django.conf import settings

from .views import HomeView,CartView,CheckoutView,ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('contact/', ContactView.as_view(), name='contact'),
]