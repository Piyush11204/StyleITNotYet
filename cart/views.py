from django.shortcuts import render ,get_object_or_404
from .cart import Cart
from  home.models import ShopIT
from django.http import JsonResponse

def cart_summary(request):
    return  render(request, 'cart',{})

def cart_add(request):
    cart =  Cart(request)
    if request.POST.get('action')=='post':
        ShopIT_id=str(request.POST.get('ShopIT_id'))

        shopIT = get_object_or_404(ShopIT, id=ShopIT_id)
        cart.add(ShopIT=shopIT)

        cart_quantity=cart.__len__()
        # response =JsonResponse({'Product Name:': ShopIT.name })
        response =JsonResponse({'qty:': cart_quantity })
        return response()
    
    
    

def cart_delete(request):
    pass

def cart_update(request):
    pass