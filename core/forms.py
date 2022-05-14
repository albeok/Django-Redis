from django import forms
from products.models import Lot

class HashLotModelForm(forms.ModelForm):

    class Meta:
        model = Lot
        fields = ['hash']