from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")      

def list_product(request):
    """_summary_
    returns product list page
    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return render(request,"product_list.html")

def list_product(request):
    return render(request,"product_detail.html")