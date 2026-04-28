from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BrandViewSet, ProductViewSet, CustomerViewSet

r = DefaultRouter()
r.register("category", CategoryViewSet)
r.register("brand", BrandViewSet)
r.register("product", ProductViewSet)
r.register("customer", CustomerViewSet)

urlpatterns = [
    path('', include(r.urls)),
]