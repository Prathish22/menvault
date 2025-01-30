from django.shortcuts import render, redirect
from . models import Order, OrderItem
from customer.models import Customer
from products.models import Product

# def show_cart(request):
    # user1=request.user
    # customer_profile = Customer.objects.create(user=user1)
    # customer=user1.customer_profile
    # cart_obj,created=Order.objects.get_or_create(
    #         owner=customer,
    #         order_status=Order.CART_STAGE       ------------ mine
    #     )
    # context={'cart':cart_obj}
    # return render(request,'cart.html')
       
# def show_cart(request):
#     user=request.user
#     customer=user.customer_profile
#     print("user",user)
#     print("customer",customer)
#     cart_obj,created=Order.objects.get_or_create(               ------------ mine
#             owner=customer,
#             order_status=Order.CART_STAGE
#         )
#     context={'cart':cart_obj}
#     return render(request,'cart.html',context)  


# def add_tocart(request):
#     if request.POST:
#         user=request.user
#         print(user)
#         customer=user.customer_profile
#         print(customer)
#         quantity=int(request.POST.get('quantity'))
#         product_id=request.POST.get('product_id')
#         cart_obj,created=Order.objects.get_or_create(
#             owner=customer,
#             order_status=Order.CART_STAGE
#         )
#         product=Product.objects.get(pk=product_id)
#         ordered_item=OrderItem.objects.create(
#             product=product_id,
#             quantity=quantity,
#             owner=cart_obj
#         )
#         return redirect('cart')    ===================================================
    

# def show_cart(request):
#     user=request.user
#     customer=user.customer_profile
#     print("user",user)
#     print("customer",customer)
#     cart_obj,created=Order.objects.get_or_create(
#             owner=customer,
#             order_status=Order.CART_STAGE
#         )
#     context={'cart':cart_obj}

#     return render(request,'cart.html',context)

# def add_tocart(request):
#     if request.POST:
#         user=request.user                                  brokart
#         print(user)
#         customer=user.customer_profile
#         print(customer)
#         quantity=int(request.POST.get('quantity'))
#         product_id=request.POST.get('product_id')
#         cart_obj,created=Order.objects.get_or_create(
#             owner=customer,
#             order_status=Order.CART_STAGE
#         )
#         product=Product.objects.get(pk=product_id)
#         ordered_item,created=OrderItem.objects.get_or_create(
#             product=product,
#             owner=cart_obj
#         )                                                                  ===================================================
#         return redirect('cart')


def show_cart(request):
    user = request.user
    # Ensure the user has a customer_profile
    if not hasattr(user, 'customer_profile'):
        customer = Customer.objects.create(user=user)
    else:
        customer = user.customer_profile

    print("user", user)
    print("customer", customer)
    cart_obj, created = Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE
    )
    context = {'cart': cart_obj}

    return render(request, 'cart.html', context)

def add_tocart(request):
    if request.POST:
        user = request.user
        # Ensure the user has a customer_profile
        if not hasattr(user, 'customer_profile'):
            customer = Customer.objects.create(user=user)
        else:
            customer = user.customer_profile

        print(user)
        print(customer)
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')
        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        product = Product.objects.get(pk=product_id)
        ordered_item, created = OrderItem.objects.get_or_create(
            product=product,
            owner=cart_obj
        )

    return redirect('cart')


   



        