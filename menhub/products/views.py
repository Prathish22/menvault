from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request,"index.html")      

def list_products(request):
    """_summary_
    returns product list page
    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    # product_list=Product.objects.all()
    # product_paginator=Paginator(product_list,2)
    # product_list=product_paginator.get_page(1)
    # context={'products':product_list}
    # return render(request,"products.html",context)
# def product_list(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    products = Product.objects.all() 
    product_paginator=Paginator(products,3)
    products=product_paginator.get_page(page) 
    return render(request, 'products.html', {'products': products})



def detail_product(request):
    if request.POST:
        print(request.POST)
    return render(request,"product_detail.html")


