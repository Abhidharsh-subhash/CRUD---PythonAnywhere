from django.shortcuts import render,get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Products

# Create your views here.

class Product_crud(GenericAPIView):
    serializer_class=ProductSerializer
    queryset=Products.objects.all()
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        data=request.data.get('product_id')
        if data:
            product=get_object_or_404(Products,pk=data)
            serializer=self.serializer_class(instance=product)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        serializer=self.serializer_class(instance=self.get_queryset(),many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def patch(self,request):
        data=request.data.get('product_id')
        if not data:
            response={
                'message':'product_id is required in the request body'
            }
            return Response(data=response,status=status.HTTP_400_BAD_REQUEST)
        product=get_object_or_404(Products,pk=data)
        serializer=self.serializer_class(instance=product,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            response={
                'message':'Product details updates successfully',
                'data':serializer.data
            }
            return Response(data=response,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request):
        data=request.data.get('product_id')
        if not data:
            response={
                'message':'product_id is required in the request body'
            }
            return Response(data=response,status=status.HTTP_400_BAD_REQUEST)
        product=get_object_or_404(Products,pk=data)
        product.delete()
        response={
            'message':'Product deleted successfully'
        }
        return Response(data=response,status=status.HTTP_204_NO_CONTENT)




