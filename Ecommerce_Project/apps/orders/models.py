from django.db import models
# from Ecommerce_Project.apps.core.models import *
# from Ecommerce_Project.apps.vendors.models import *
from django.contrib.auth.models import User
# Create your models here.

class OrderDetail(models.Model):
    order_id = models.ForeignKey('orders.Order',on_delete=models.CASCADE)
    order_detail_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey('core.Product',on_delete=models.CASCADE)
    product_quantity = models.IntegerField()

    def __str__(self):
        return str(self.order_detail_id)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_no = models.IntegerField()
    ordered_date = models.DateTimeField(auto_now_add=True)
    total_order = models.IntegerField()
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    shipping_date = models.DateField(auto_now_add=True)
    order_status = models.CharField(max_length=10)
    order_detail = models.ForeignKey('orders.OrderDetail',on_delete=models.CASCADE)


    def __str__(self):
        return str(self.order_id)

