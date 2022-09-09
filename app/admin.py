from django.contrib import admin
from .models import SupplierDetails, ShopInventory,ProductSells,HoleSaleBuyInfo

# Register your models here.
admin.site.register(SupplierDetails)
admin.site.register(ShopInventory)
admin.site.register(ProductSells)
admin.site.register(HoleSaleBuyInfo)