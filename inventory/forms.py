from django import forms
from models import Products

class ProductUploadForm(forms.ModelForm):
    class Meta:
        models = Products
        fields = "__all__"
