from django.shortcuts import render
from .models import SupplierDetails, ShopInventory, ProductSells, HoleSaleBuyInfo
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import SupplierDetailsSerializer, ShopInventorySerializer, HoleSaleBuyInfoSerializer, ProductSellsSerializer
from rest_framework import status
# Create your views here.

class GlocerySupplier(viewsets.ViewSet):

    def list(self, request):
        products = SupplierDetails.objects.all()
        s_data = SupplierDetailsSerializer(products, many=True)
        return Response(s_data.data)
    
 
    def create(self, request):
        product = SupplierDetailsSerializer(data=request.data)
        if product.is_valid():
            product.save()
            return Response(product.data, status=status.HTTP_201_CREATED)
        return Response (product.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def put(self, request):
        product = SupplierDetailsSerializer(data=request.data)
        return Response(product.data, status=status.HTTP_201_CREATED)
        

    def delete(self, request):
        product = SupplierDetailsSerializer(data=request.data)
        return Response({"messege":"product is deleted successfully"}) 


