from pyexpat import model
from django.db import models
import uuid
# Create your models here.
PRODUCT = (
    ('glocery', 'glocery'),
    ('stationary', 'stationary'),
    ('electronic', 'electronic'),
)

class SupplierDetails(models.Model):
    supplier_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    category = models.CharField(max_length=255, choices= PRODUCT)
    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class ShopInventory(models.Model):
    product_name = models.CharField(max_length=255, null=False)
    product_quantity = models.CharField(max_length=255)
    buy_price = models.CharField(max_length=255)
    sell_price = models.CharField(max_length=255)
    product_remain = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class ProductSells(models.Model):
    product_name = models.CharField(max_length=255, null=False)
    customer_name = models.CharField(max_length=255, null=False)
    sells_quantity = models.CharField(max_length=255, null=False)
    product_price = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class HoleSaleBuyInfo(models.Model):
    customer_id = models.ForeignKey(SupplierDetails, on_delete=models.CASCADE)
    purchase_quantity = models.CharField(max_length=255)
    paid_amount = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)



