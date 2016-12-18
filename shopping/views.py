from django.shortcuts import render
from .models import Product
from tango_with_django_project.settings import BASE_DIR
from django.http import HttpResponse
# Create your views here.


def index(request):
    products = Product.objects.all()
    context_dict = {'products': products, 'DIR': BASE_DIR}

    return render(request, 'shopping/index.html', context_dict)

def image(request, path):
    return HttpResponse()