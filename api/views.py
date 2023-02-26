from django.shortcuts import render
from api.serializers import ProductSerialiser
from product.models import Product
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import status

# Create your views here.

class ProductsView(APIView):
    def get(self,request):
        
        queryset=Product.objects.all().order_by("name")
        serializer=ProductSerialiser(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request): 
        serializer=ProductSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED )
        else:
            return  Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

      



class PrductView(APIView):
    def single_product(self,item_id) :
        try:
          queryset=Product.objects.get(id=item_id)
          
          return queryset
        except Product.DoesNotExist :
           return None

    def get(self,request,item_id):
        queryset=self.single_product(item_id)
        if queryset:

            serializer=ProductSerialiser(queryset)
            return Response(serializer.data)
        else :
            #handel_resonse For no exist id
            return Response({"msg":f'This id {item_id} not exist'},status.HTTP_400_BAD_REQUEST)
        




