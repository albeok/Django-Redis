from pyexpat import model
from django import forms
from .models import Lot

class LotModelForm(forms.ModelForm):

    class Meta:
        model = Lot
        fields = "__all__"
        exclude = ["image", "generic_info", "hash", "tx_id"]
