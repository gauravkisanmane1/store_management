from rest_framework import serializers
from app.models import SupplierDetails, ShopInventory, ProductSells, HoleSaleBuyInfo


class SupplierDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierDetails
        fields = '__all__'

class ShopInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopInventory
        fields = '__all__'

class ProductSellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSells
        fields = '__all__'

class HoleSaleBuyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoleSaleBuyInfo
        fields = '__all__'

