from django import forms
from .models import ItemInOrder


class AddItemToOrder(forms.ModelForm):

    quantity = forms.IntegerField(
        required=True,
        widget=forms.widgets.NumberInput(
            attrs={
                'class': 'input is-success is-normal',
            }
        ),
    )

    class Meta:
        model = ItemInOrder
        fields = ['quantity']