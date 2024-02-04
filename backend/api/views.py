from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Product
from .serializer import ProductsSerializer


# Create your views here.
class ProductView(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
        



