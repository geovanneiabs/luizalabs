from django.shortcuts import render

# Create your views here.
from store.models import Client, Product, Review, ListProduct
from rest_framework import viewsets
from rest_framework import permissions
from store.serializers import ClientSerializer, ProductSerializer, ReviewSerializer, ListProductSerializer


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Client.objects.all().order_by('nome')
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('title')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReviewViewSet(viewsets.ModelViewSet):    
    queryset = Review.objects.all().order_by('product__title')
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductListViewSet(viewsets.ModelViewSet):    
    queryset = ListProduct.objects.all()
    serializer_class = ListProductSerializer
    permission_classes = [permissions.IsAuthenticated]




    
    