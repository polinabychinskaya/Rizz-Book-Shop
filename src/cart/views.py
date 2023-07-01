from typing import Any, Dict, Optional
from django.db import models
from django.shortcuts import render
from  django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, FormView, ListView, UpdateView, DeleteView
from . import models
from reference.models import Title
from cart.models import Status
from django.shortcuts import get_object_or_404
from . import models, forms
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class CartDetailView(DetailView):
    template_name = 'cart/cart.html'
    model = models.Cart

    def get_object(self, *args, **kwargs):
        pk = self.request.session.get('cart_id')
        customer = self.request.user
        if customer.is_anonymous:
            customer = None
        cart, created = models.Cart.objects.get_or_create(
            pk=pk,
            defaults={
                'customer': customer
            }
        )

        quantity = self.request.GET.get('quantity')
        item_id = self.request.GET.get('item_id')
        if quantity and item_id:
            quantity = int(quantity)
            item = Title.objects.get(pk=int(item_id))
            price = item.price
            item_in_cart, item_in_cart_created = models.ItemsInCart.objects.get_or_create(
                cart = cart,
                item = item,
                defaults={
                    'quantity':quantity,
                    'price':price*quantity
                }
            )

            if not item_in_cart_created:
                item_in_cart.quantity = item_in_cart.quantity + quantity
                item_in_cart.price = item_in_cart.price + price*quantity
                item_in_cart.save()

            if created:
                self.request.session['cart_id'] = cart.pk
        return cart
    
class CartAddDeleteView(DetailView):
    template_name = 'cart/cart.html'
    model = models.Cart

    def get_object(self, *args, **kwargs):
        cart_pk = self.request.session.get('cart_id')
        customer = self.request.user
        if customer.is_anonymous:
            customer = None
        cart, created = models.Cart.objects.get_or_create(
            pk=cart_pk,
            defaults={
                'customer': customer
            }
        )
        
        item_id = self.request.GET.get("item")
        action = self.request.GET.get("action")
        if item_id and action and action in ['add', 'delete']:
            item = Title.objects.get(pk=int(item_id))
            price = item.price
            item_in_cart = get_object_or_404(
                models.ItemsInCart,
                cart__pk=cart.pk,
                item__pk=item.pk,
            )
            if action == "add":
                addendum = 1
            else:
                if item_in_cart.quantity <= 1:
                    item_in_cart.delete()
                    return cart
                addendum = -1
            item_in_cart.quantity = item_in_cart.quantity + addendum
            item_in_cart.price = item_in_cart.quantity * price
            item_in_cart.save()
        return cart
    
#---------SUCCESS PAGE---------#

def success_order(request):
    return render(
        request,
        template_name='cart/order_success.html'
    )
    
class CreateOrder(FormView):
    form_class = forms.CreateOrderForm
    template_name = 'cart/createorder.html'
    success_url = reverse_lazy('cart:success-order')
    def form_valid(self, form):
        user = self.request.user
        phone = form.cleaned_data.get('phone')
        payment_method = form.cleaned_data.get('payment_method')
        address = form.cleaned_data.get('address')
        status = Status.objects.get(pk=settings.ORDER_STATUS_NEW)
        cart_pk = int(self.request.session.get('cart_id'))
        cart = models.Cart.objects.get(pk=cart_pk)
        cart = get_object_or_404(
            models.Cart,
            pk=cart_pk
        )
        models.Order.objects.create(
            user = user,
            phone=phone,
            payment_method=payment_method,
            address=address,
            status=status,
            cart=cart
        )
        del self.request.session['cart_id']
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id', -100)
        context['object'] = get_object_or_404(
            models.Cart,
            pk=int(cart_id)
        )
        return context
    
class OrderListView(LoginRequiredMixin, ListView):
    model = models.Order
    template_name = 'cart/admin_orders.html'
    login_url = reverse_lazy('roles:login')

class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Order
    fields = [
        'phone', 
        'address', 
        'status', 
        'payment_method'
    ]
    template_name = 'cart/admin_orders_update.html'
    login_url = reverse_lazy('roles:login')

class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Order
    template_name = 'cart/admin_orders_delete.html'
    success_url = '/success'
    login_url = reverse_lazy('roles:login')

def open_orders(request):
    user_id = request.user.id
    orders = models.Order.objects.filter(user_id = user_id)
    context = {'orders': orders}
    return render(request, 'cart/open_orders.html', context)

