from django import forms
from models import Delivery

class DeliveryUploadForm(forms.ModelForm):
    class Meta:
        models = Delivery
        fields = "__all__"
