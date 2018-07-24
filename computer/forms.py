from django import forms
from computer.models import Item


class computerForm(forms.ModelForm):
    item = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ))

    class Meta:
        model = Item
        fields = ('item_name','item_price','item_status')
