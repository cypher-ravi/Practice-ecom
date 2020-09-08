from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=20)
    category_publish_data = models.DateTimeField(auto_now_add=True)
    category_status = models.CharField(max_length=20)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Image = models.ImageField()

    def __str__(self):
        return self.category_name

    class Meta:
         verbose_name_plural= 'Categories'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_image = models.ImageField()
    product_company = models.CharField(max_length=50)
    product_publish_date = models.DateTimeField(auto_now_add=True)
    admin_id = models.ForeignKey(User,on_delete=models.CASCADE)
    product_regular_price = models.FloatField()
    product_discount_price = models.FloatField()
    product_stock_quantity = models.IntegerField()
    #product_status = TODO:status field

    def __str__(self):
        return self.product_name

    class Meta:
         verbose_name_plural = 'Products'


class ProductInfo(models.Model):
    """

    This model Take care of description of product
    For ex:Samsung G-series, A-series

    """
    model_id  = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=20)
    model_status = models.CharField(max_length=20)
    model_publish_date = models.DateTimeField(auto_now_add=True)
    model_description = models.CharField(max_length=20)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE)
    model_image = models.ImageField()
    model_price = models.FloatField()
     #TODO:status field
    model_stock_quantity = models.IntegerField()


    def __str__(self):
        return self.model_name

    class Meta:
        verbose_name_plural = 'Product Model'

    
class EachModelSpecification(models.Model):
    """
    It will Take care of specifications of each model of each product  

    """

    spec_id = models.AutoField(primary_key=True)
    model_id = models.ForeignKey(ProductInfo, on_delete=models.CASCADE)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE)
    spec_name = models.CharField(max_length=20)
    spec_publish_date = models.DateTimeField(auto_now_add=True)
    spec_status = models.CharField(max_length=20)
    #TODO:status field
    def __str__(self):
        return self.spec_name

    class Meta:
        verbose_name_plural = 'Specification'

class EachSpecificationValue(models.Model):
    """

    Here we insert value for each specification

    """
    spec_value_id = models.AutoField(primary_key=True)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE)
    spec_id = models.ForeignKey(EachModelSpecification, on_delete=models.CASCADE)
    spec_value = models.CharField(max_length=100)

    def __str__(self):
        return self.spec_value

    class Meta:
        verbose_name_plural = 'Specification values'



# class Status(models.Model):
#     status_id = models.AutoField(primary_key=True)
#     status_value = models.B()

#     def __str__(self):
#         return str(self.status_id)

# class Statusvalue(models.Model):
#     status_value_id = models.AutoField(primary_key=True)
#     is_

