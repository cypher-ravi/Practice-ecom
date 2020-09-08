from django.urls import path,include
from django.conf import settings

from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]