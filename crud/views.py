from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer

# Create your views here.

class Product_crud(GenericAPIView):
    pass



