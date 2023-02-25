from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Item, ItemInOrder, Tax, Discount, Order
from .forms import AddItemToOrder
import stripe
from urllib.parse import unquote
import json

stripe.api_key = settings.STRIPE_SECRET_KEY
public_key = settings.STRIPE_PUBLISHABLE_KEY


def item_list(request):
    items = [item for item in Item.objects.all()]
    return render(request, './templates/items_list.html', {'items': items})


def item_page(request, pk):
    item = Item.objects.get(pk=pk)
    taxes = Tax.objects.all()
    coupons = Discount.objects.all()
    return render(request, 'item_template.html',
                  {'item': item, 'public_key': public_key, 'taxes': taxes, 'coupons': coupons})


def buy(request, pk):
    item = Item.objects.get(pk=pk)
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': item.get_price_data,
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/success/',
        cancel_url='http://localhost:8000/cancel/',
    )

    return JsonResponse({'session_id': session.id})


def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')


def add_item_to_order(request, pk):
    form = AddItemToOrder(request.POST or None)
    if request.method == "POST" and form.is_valid():
        order = None
        if Order.objects.filter(customer=request.user).exists():
            order = Order.objects.get(customer=request.user)
        else:
            order = Order.objects.create(customer=request.user)
        order.items.filter(item=Item.objects.get(pk=pk))
        if order.items.filter(item=Item.objects.get(pk=pk)).exists():
            item_in_order = order.items.get(item=Item.objects.get(pk=pk))
            item_in_order.quantity += form.cleaned_data['quantity']
            item_in_order.save()
            order.save()
        else:
            order.items.create(
                item=Item.objects.get(pk=pk),
                quantity=int(form.cleaned_data['quantity']),
                order=order,
            )
        return redirect("item_page", pk=pk)
    return render(request, 'add_item_to_order.html', {'form': form, 'item': Item.objects.get(pk=pk)})


def order_list(request):
    order = Order.objects.get(customer=request.user)
    taxes = Tax.objects.all()
    coupons = Discount.objects.all()
    return render(request, 'order_list.html',
                  {'order': order, 'public_key': public_key, 'taxes': taxes, 'coupons': coupons})


def buy_order(request):
    order = Order.objects.get(customer=request.user)
    encoded_data = request.GET.get('data')
    if encoded_data:
        decoded_data = json.loads(unquote(encoded_data))
        selected_tax = decoded_data['tax_id']
        selected_coupon = decoded_data['coup_id']
        order.tax = Tax.objects.get(tax_id=selected_tax)
        order.discount = Discount.objects.get(discount_id=selected_coupon)
        order.save()

        session = stripe.checkout.Session.create(
            line_items=order.get_line_items,
            mode='payment',
            discounts=[{
                'coupon': order.discount.discount_id,
            }],
            success_url='http://localhost:8000/success/',
            cancel_url='http://localhost:8000/cancel/',
        )

    return JsonResponse({'session_id': session.id})


def clear_order(request):
    order = Order.objects.get(customer=request.user)
    order.items.all().delete()
    return redirect('item_list')
