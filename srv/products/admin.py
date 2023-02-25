from django.contrib import admin
from .models import Item, ItemInOrder, Tax, Discount, Order
# Register your models here.


class ItemInOrderInline(admin.TabularInline):
    model = ItemInOrder


class OrderAdmin(admin.ModelAdmin):
    inlines = [ItemInOrderInline]


admin.site.register(Item)
admin.site.register(ItemInOrder)
admin.site.register(Order, OrderAdmin)
admin.site.register(Tax)
admin.site.register(Discount)
