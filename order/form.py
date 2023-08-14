from django import forms
from models import Order

class OrderUploadForm(forms.ModelForm):
    class Meta:
        models = Order
        fields = "__all__"
