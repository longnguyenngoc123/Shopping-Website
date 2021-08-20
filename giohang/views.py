from django.shortcuts import render, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from monan.models import Post
from .models import Cart
from django.urls import reverse 
# Create your views here.
@login_required
def index(request):
    try:
        the_id  = request.session['cart_id']
    except:
        the_id = None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {"cart": cart}
    else:
        empty = "Please keep shopping, you havent buy anything yet"
        context = {"empty":empty}
    template = "shop/views.html"
    return render(request, template,context)
@login_required
def update_cart(request, id):
    request.session.set_expiry(300)
    try:
        the_id = request.session['cart_id'] 
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    cart = Cart.objects.get(id=the_id)
    try:
        product = Post.objects.get(id=id)
    except:
        pass
    cart.product.add(product)
    new_total = 0.00
    for item in cart.product.all():
        new_total += float(item.price)
    cart.total = new_total
    cart.product.add(product)
    cart.save()
    return HttpResponseRedirect('/')
@login_required
def delete_cart(request, id):
    cart = Cart.objects.all()[0]
    try:
        product = Post.objects.get(id=id)
    except:
        pass
    cart.product.remove(product)
    new_total = 0.00
    for item in cart.product.all():
        new_total += float(item.price)
    cart.total = new_total
    cart.save()
    return HttpResponsePermanentRedirect(reverse("giohang"))

