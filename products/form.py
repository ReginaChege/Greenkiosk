from django import forms
from models import Product

class ProductUploadForm(forms.ModelForm):
    class Meta:
        models = Product
        fields = "__all__"
