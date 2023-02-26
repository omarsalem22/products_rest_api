from django.shortcuts import render
from api.serializers import ProductSerialiser
from product.models import Product
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


