from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def show_account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            password=request.POST.get('password')
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            customer=Customer.objects.create_user(
                user=user,
                phone=phone,
                address=address
            )
            success_message="Registration Successfull"
            messages.success(request,success_message)
   
        except Exception as e:
            error_message="Username already taken or Invalid username"
            messages.error(request,error_message)
        return render(request,'account.html')
        
    if request.POST and 'login' in request.POST: 
            context['register']=False 

            print(request.POST)
            username=request.POST['username']
            password=request.POST['password']
            print(username,password)
            user=authenticate(username=username,password=password)
            print(user)
            if user:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'Invalid user login')        

    return render(request,'account.html', context)


def signout(request):
    logout(request)
    return redirect ('home')


