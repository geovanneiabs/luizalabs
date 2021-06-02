from rest_framework import serializers
from store.models import Client, Product, Review, ListProduct#, ListItems

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('nome','email')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','title','product_code','brand','price','image')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('product','client','note')

class ListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListProduct
        fields = ('id','client','product')




        
        

       