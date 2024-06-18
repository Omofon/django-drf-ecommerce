from rest_framework.response import Response
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer


# Create your views here.
class CategoryViewset(viewsets.ViewSet):
    """
    A simple Viewset for viewing all categories
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serialized_data = CategorySerializer(self.queryset, many=True)
        return Response(serialized_data.data)


class BrandViewset(viewsets.ViewSet):
    """
    A simple Viewset for viewing all brands
    """

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serialized_data = BrandSerializer(self.queryset, many=True)
        return Response(serialized_data.data)


class ProductViewset(viewsets.ViewSet):
    """
    A simple Viewset for viewing all products
    """

    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serialized_data = ProductSerializer(self.queryset, many=True)
        return Response(serialized_data.data)
