from django import forms
from models import Payment

class PaymentUploadForm(forms.ModelForm):
    class Meta:
        models = Payment
        fields = "__all__"
