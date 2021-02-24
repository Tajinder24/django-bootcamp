from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Product

# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World!!</h1>")


def product_detail_view(request, pk):
    try:     
        obj = Product.objects.get(id = pk)
    except Product.DoesNotExist:
        raise Http404 #Render html page with HTTP Status code of404
    return HttpResponse(f"<h1> Product id - {obj.id} </h1>")

class HomeView:
    pass