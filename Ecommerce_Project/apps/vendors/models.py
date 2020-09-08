from django.db import models
# import Ecommerce_Project.apps.core.models 
# import Ecommerce_Project.apps.orders.models 
# from django_countries.fields import CountryField
# from cities.models import BaseCountry
# from django.apps import apps
# order_models = apps.get_model('')
from phonenumber_field.modelfields import PhoneNumberField
# from Ecommerce_Project.apps import core
# from Ecommerce_Project.apps import orders


GENDER_CHOICES = (
    ("1", "Please Select"),
    ("2", "Male"),
    ("3", "Female"),
    ("4", "Other"),

)

STATUS_CHOICES = (
    ("1", "Please Select"),
    ("2", "New"),
    ("3", "Verified"),

)

VALID_STATE_CHOICES = (
    ("1", "Please Select"),
    ("2", "Andra Pradesh"),
    ("3", "Arunachal Pradesh"),
    ("4", "Assam"),
    ("5", "Bihar"),
    ("6", "Chhattisgarh"),
    ("7", "Chandigarh"),
    ("8", "Dadar and Nagar Haveli"),
    ("9", "Daman and Diu"),
    ("10", "Delhi"),
    ("11", "Goa"),
    ("12", "Gujarat"),
    ("13", "Haryana"),
    ("14", "Himachal Pradesh"),
    ("15", "Jammu and Kashmir"),
    ("16", "Jharkhand"),
    ("17", "Karnataka"),
    ("18", "Kerala"),
    ("19", "Lakshadeep"),
    ("20", "Madya Pradesh"),
    ("21", "Maharashtra"),
    ("22", "Manipur"),
    ("23", "Meghalaya"),
    ("24", "Mizoram"),
    ("25", "Nagaland"),
    ("26", "Orissa"),
    ("27", "Punjab"),
    ("28", "Pondicherry"),
    ("29", "Rajasthan"),
    ("30", "Sikkim"),
    ("31", "Tamil Nadu"),
    ("32", "Telagana"),
    ("33", "Tripura"),
    ("34", "Uttaranchal"),
    ("35", "Uttar Pradesh"),
    ("36", "West Bengal"),
    ("37", "Andaman and Nicobar Island"),

)



class VendorDetail(models.Model):
    vendor_detai_id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=50, default='')
    Company_Name = models.CharField(max_length=100, default='')
    Busniess_Type = models.ForeignKey('core.Category' , on_delete=models.CASCADE, related_name='category')
    Service_decsription = models.TextField(max_length=1000, default='')
    Mobile_No = PhoneNumberField()
    Mobile_No_2 = PhoneNumberField()
    Address1 = models.CharField(max_length=100, default='')
    Address2 = models.CharField(max_length=100, blank=True, null=True, default='')
    # country = CountryField()
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, choices=VALID_STATE_CHOICES, default='Please Select')
    PinCode = models.IntegerField()
    Contact_Person = models.CharField(max_length=100, default='', blank=True, null=True)
    EmailID = models.EmailField(null=True, blank=True)
    Landline = PhoneNumberField(null=True)
    GST_No = models.IntegerField(null=True, blank=True)
    Pan_No = models.IntegerField(null=True, blank=True)
    TIN_No = models.IntegerField(null=True, blank=True)
    Registered_Trade_Name = models.CharField(max_length=100, blank=True, null=True, default='')
    Facebook_URL = models.URLField(max_length=200, blank=True, null=True)
    Twitter_URL = models.URLField(max_length=200, blank=True, null=True)
    website_URL = models.URLField(max_length=200, blank=True, null=True)
    Status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    Other_Info = models.CharField(max_length=200, blank=True, null=True)
    Discount_Percentage = models.IntegerField(null=True)
    Longitude = models.FloatField(null=True, blank=True)
    Latitude = models.FloatField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    Image = models.ImageField()


    class Meta:
        verbose_name_plural = 'Vendor Details'



# Create your models here.
class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    vendor_detail = models.ForeignKey(VendorDetail,on_delete=models.CASCADE)
    category = models.ForeignKey('core.Category',on_delete=models.CASCADE)
    products = models.ForeignKey('core.Product',on_delete=models.CASCADE)
    orders = models.ForeignKey('orders.Order',on_delete=models.CASCADE)
    

    def __str__(self):
        return self.vendor_detail.vendor_name

