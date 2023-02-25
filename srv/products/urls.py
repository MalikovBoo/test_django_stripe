from django.urls import path
from .views import item_list, item_page, buy, success, cancel, add_item_to_order, order_list, buy_order, clear_order

from . import views

urlpatterns = [
    path('', item_list, name='item_list'),
    path('item/<int:pk>', item_page, name='item_page'),
    path('item/<int:pk>/add_to_order', add_item_to_order, name='add_item_to_order'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
    path('buy/<int:pk>', buy, name='buy'),
    path('order_list', order_list, name='order_list'),
    path('buy_order', buy_order, name='buy_order'),
    path('clear_order', clear_order, name='clear_order'),
]
