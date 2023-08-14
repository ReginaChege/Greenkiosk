from django.shortcuts import render

# Create your views here.
from .forms import VendorUploadForm
def upload_vendor(request):
    form = VendorUploadForm()
    return render(request, "inventory/product_upload.html",{'form':form})
    

def vendor_list(request):
   vendor= vendor.objects.all()
   return render(request, "inventory/vendor_list.html",{'vendor':vendor})
    

def vendor_details_view (request):
   vendor=vendor.objects.get(id=id)
   return render(request, "inventory/vendor_details.html",{'vendor':vendor})
    