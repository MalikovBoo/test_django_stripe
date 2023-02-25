from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=100, default='Product')
    description = models.CharField(max_length=500, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name + ', price: ' + str(self.price)

    @property
    def get_price(self):
        return self.price*100

    @property
    def get_price_data(self):
        price_data = {
            'currency': 'usd',
            'product_data': {
                'name': self.name,
                'description': self.description,
            },
            'unit_amount': self.get_price,
        }
        return price_data


class Discount(models.Model):
    discount_id = models.CharField(max_length=100)
    discount_name = models.CharField(max_length=100, default='discount')

    def __str__(self):
        return self.discount_name


class Tax(models.Model):
    tax_id = models.CharField(max_length=100)
    tax_name = models.CharField(max_length=100, default='tax')

    def __str__(self):
        return self.tax_name


class Order(models.Model):
    customer = models.ForeignKey(User, related_name='order', on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, blank=True, null=True)
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, blank=True, null=True)

    @property
    def total(self):
        result = 0
        for item in self.items:
            result += item.item.price * item.quantity
        return result

    @property
    def get_line_items(self):
        line_items = []
        for item in self.items.all():
            line_items.append({
                'price_data': item.item.get_price_data,
                'quantity': item.quantity,
                'tax_rates': [self.tax.tax_id],
            })
        return line_items

    def __str__(self):
        return 'order of ' + str(self.customer)


class ItemInOrder(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, related_name='item_in_order', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return 'item ' + str(self.item) + ' quantity:' + str(self.quantity)
