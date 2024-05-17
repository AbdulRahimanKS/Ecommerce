from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from shop.models import *
from . models import *

# Create your views here.

def cart_details(request, total = 0, count = 0):
    ct_items = None
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
        ct_items = items.objects.filter(cart = ct, active = True)

        for item in ct_items:
            total += (item.product.price * item.quantity)
            count += item.quantity

    except ObjectDoesNotExist:
        pass

    return render(request, 'cart.html', {'ct': ct_items, 'tot': total, 'cn': count})


def c_id(request):
    if request.user.is_authenticated:
        return str(request.user.id)
    else:
        ct_id = request.session.session_key
        if not ct_id:
            ct_id = request.session.create()
        return ct_id

def add_cart(request, product_id):
    prod = products.objects.get(id = product_id)
    try:
        ct = cartlist.objects.get(cart_id = c_id(request))
    except cartlist.DoesNotExist:
        ct = cartlist.objects.create(cart_id = c_id(request))
        ct.save()
    try:
        c_items = items.objects.get(product = prod, cart = ct)
        if c_items.quantity < c_items.product.stock:
            c_items.quantity += 1
            c_items.save()
    except items.DoesNotExist:
        c_items = items.objects.create(product = prod,  quantity = 1, cart = ct)
        c_items.save()
    return redirect('cartDetails')

def min_cart(request, product_id):
    ct = cartlist.objects.get(cart_id = c_id(request))
    prod = get_object_or_404(products, id = product_id)
    c_items = items.objects.get(product = prod, cart = ct)

    if c_items.quantity > 1:
        c_items.quantity -= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartDetails')

def del_cart(request, product_id):
    ct = cartlist.objects.get(cart_id = c_id(request))
    prod = get_object_or_404(products, id = product_id)
    c_items = items.objects.get(product = prod, cart = ct)

    c_items.delete()
    return redirect('cartDetails')
