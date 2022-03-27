from main_app.models import Product
from main_app.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class ProductApi(APIView):
    def get(request, self, pk=None, format=None):
        id = pk
        if id is not None:
            comp_obj = Product.objects.get(id=id)
            serializer = ProductSerializer(comp_obj)
            return Response(serializer.data)
        comp_obj = Product.objects.all()
        serializer = ProductSerializer(comp_obj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        comp_obj = Product.objects.get(id=pk)
        serializer = ProductSerializer(comp_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        comp_obj = Product.objects.get(id=pk)
        serializer = ProductSerializer(comp_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(request, self, pk, format=None):
        comp_obj = Product.objects.get(id=pk)
        comp_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)