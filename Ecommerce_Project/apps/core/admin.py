from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(ProductInfo)
admin.site.register(Category)
admin.site.register(EachModelSpecification)
admin.site.register(EachSpecificationValue)