from django.shortcuts import render, redirect
from . models import Order, OrderItem
from . models import Customer,Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def show_cart(request):
    user=request.user
    customer = user.customer_profile
    print("user",user)
    print("customer",customer)
    cart_obj,created=Order.objects.get_or_create(              
            owner=customer,
            order_status=Order.CART_STAGE
    )
    total_price = 0
    for item in cart_obj.added_items.all():
        total_price += item.quantity * item.product.price
    
    context = {'cart': cart_obj, 'total_price': total_price }
    # context={'cart':cart_obj}
    print(cart_obj)
    return render(request,'cart.html',context) 



def add_tocart(request):
    if request.POST:
        user=request.user
        print('user',user)
    try:
        customer = user.customer_profile
    except Customer.DoesNotExist:
        customer = Customer.objects.create(user=user)

    quantity = int(request.POST.get('quantity'))
    print('quantity',quantity)
    # if quantity <= 0:
    #     return HttpResponse("Invalid quantity")
    product_id=request.POST.get('product.id')
    print('product_id',product_id)
    cart_obj,created=Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE
    )
    product=Product.objects.get(pk=product_id)
    print('product',product)
    ordered_item,created=OrderItem.objects.get_or_create(
        product=product,
        owner=cart_obj
    )
    if created:
        ordered_item.quantity=quantity
        ordered_item.save()
    else:
        ordered_item.quantity=ordered_item.quantity+quantity
        ordered_item.save()
    return redirect('cart')



def remove_item(request,pk):
    item=OrderItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')



def checkout(request):
    if request.POST:
        try:
            user=request.user
            customer = user.customer_profile
            total=float(request.POST.get('total'))
            order_obj=Order.objects.get(              
                owner=customer,
                order_status=Order.CART_STAGE
            )
            if order_obj:
                order_obj.status=Order.ORDER_CONFIRMED
                order_obj.total_price=total
                order_obj.save()
                order_status="Your order is confirmed! Your Order has been successfully placed and is being processed"
                messages.success(request,order_status)
            else:
                order_status="Order failed. Cart is Empty."
                messages.error(request,order_status)
        except Exception as e:
                Order_status="Order failed. Cart is Empty."
                messages.error(request,order_status)

    return redirect('cart')      
            

    
@login_required(login_url='account')
def view_orders(request):
    user1=request.user
    customer_profile = Customer.objects.create(user=user1)
    customer=user1.customer_profile
    cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE      
        )
    context={'cart':cart_obj}
    return render(request,'cart.html')
       

# @login_required(login_url='account')
def show_orders(request):
    user=request.user
    customer = user.customer_profile
    all_order=Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
    context={'orders':all_order}
    print(all_order)
    return render(request,'order.html',context) 



# def show_cart(request):
#     user1=request.user
#     customer_profile = Customer.objects.create(user=user1)
#     customer=user1.customer_profile
#     cart_obj,created=Order.objects.get_or_create(
#             owner=customer,
#             order_status=Order.CART_STAGE      
#         )
#     context={'cart':cart_obj}
#     return render(request,'cart.html')

# def add_tocart(request):
#     print("Request data:", request.POST)
#     user = request.user
#     try:
#         customer = user.customer_profile
#     except Customer.DoesNotExist:
#         customer = Customer.objects.create(user=user)

#     quantity = int(request.POST.get('quantity'))
#     if quantity <= 0:
#         return HttpResponse("Invalid quantity")

#     product_id = request.POST.get('product.id')
#     print(product_id)
#     # product_title=request.POST.get('product.title')
#     # product_price=request.POST.get('product.price')
#     # all_details = {
#     #     'product_id': product_id,
#     #     'product_title': product_title,
#     #     'product_price': product_price
#     # }
#     # print("Product Details:", all_details) 
#     # try:
#     #     product = Product.objects.get(pk=product.id)
#     #     attributes = product.__dict__
#     #     return HttpResponse(attributes)
#         # product = Product.objects.get(pk=product_id)
#         # print("Product found:", product)
#     # except Product.DoesNotExist:
#     #     print("Product not found")
#     #     return HttpResponse("Product not found")
    
#     cart_obj, created = Order.objects.get_or_create(
#         owner=customer,
#         order_status=Order.CART_STAGE
#     )
#     ordered_item = OrderItem.objects.create(
#         product=product_id,
#         quantity=quantity,
#         owner=cart_obj
#     )
    # return redirect('cart')                       ++++++++++++++deepseek
 

# def add_tocart(request):
#     user = request.user
#     try:
#         customer = user.customer_profile
#     except Customer.DoesNotExist:
#         customer = Customer.objects.create(user=user)

#     quantity = int(request.POST.get('quantity'))
#     if quantity <= 0:
#         return HttpResponse("Invalid quantity")

#     product_id = request.POST.get('product_id')
#     try:
#         product = Product.objects.get(pk=product_id)
#     except Product.DoesNotExist:
#         return HttpResponse("Product not found")

#     cart_obj, created = Order.objects.get_or_create(
#         owner=customer,
#         order_status=Order.CART_STAGE
#     )

#     ordered_item = OrderItem.objects.create(
#         product=product,
#         quantity=quantity,
#         owner=cart_obj
#     )

#     return HttpResponse("Product added to cart successfully")




# def add_tocart(request):
#     user = request.user
#     try:
#         customer = user.customer_profile
#     except Customer.DoesNotExist:
#         customer = Customer.objects.create(user=user)

#         # print(user)
#         # # customer=user.customer_profile
#         # print(customer)
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
#         return HttpResponse("Product added to cart successfully")

#         # return render(request, 'cart.html', {'cart': cart_obj})
   #===================================================
    

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


# def show_cart(request):
#     user = request.user
#     # Ensure the user has a customer_profile
#     if not hasattr(user, 'customer_profile'):
#         customer = Customer.objects.create(user=user)
#     else:
#         customer = user.customer_profile

#     print("user", user)
#     print("customer", customer)
#     cart_obj, created = Order.objects.get_or_create(
#         owner=customer,
#         order_status=Order.CART_STAGE
#     )
#     context = {'cart': cart_obj}

#     return render(request, 'cart.html', context)

# def add_tocart(request):
#     if request.POST:
#         user = request.user
#         # Ensure the user has a customer_profile
#         if not hasattr(user, 'customer_profile'):
#             customer = Customer.objects.create(user=user)
#         else:
#             customer = user.customer_profile

#         print(user)
#         print(customer)
#         quantity = int(request.POST.get('quantity'))
#         product_id = request.POST.get('product_id')
#         cart_obj, created = Order.objects.get_or_create(
#             owner=customer,
#             order_status=Order.CART_STAGE
#         )
#         product = Product.objects.get(pk=product_id)
#         ordered_item, created = OrderItem.objects.get_or_create(
#             product=product,
#             owner=cart_obj
#         )

#     return redirect('cart')


   



        