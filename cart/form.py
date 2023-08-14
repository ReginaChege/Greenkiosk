from django import forms
from models import Cart

class CartUploadForm(forms.ModelForm):
    class Meta:
        models = Cart
        fields = "__all__"
