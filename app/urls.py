from django.contrib import admin
from django.urls import path, include
from .views import GlocerySupplier
from rest_framework.routers import DefaultRouter
# urlpatterns = [
   
# ]



router = DefaultRouter()
router.register(r'product', GlocerySupplier, basename='product')
urlpatterns = router.urls