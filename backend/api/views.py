from django.shortcuts import render
#from django.http import HttpResponse, JsonResponse

from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response


from products.models import Product
from products.serializers import ProductSerializer


# Create your views here.

@api_view(['POST'])
def api_home(request,*args, **kwargs):

    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        data = serializer.data
        return Response(serializer.data)

   
    return Response({"invalid":"not good data"}, status=400)
    
""" 
 instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        
        data = ProductSerializer(instance).data """

    


