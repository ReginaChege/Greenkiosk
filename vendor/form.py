from django import forms
from models import Vendor

class VendorUploadForm(forms.ModelForm):
    class Meta:
        models = Vendor
        fields = "__all__"
