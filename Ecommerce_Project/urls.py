from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from .apps import core

from . views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Ecommerce_Project.apps.core.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__', include(debug_toolbar.urls))]