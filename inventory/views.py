from django.shortcuts import render

# Create your views here.
from .forms import ProductUploadForm
def upload_product(request):
    form = ProductUploadForm()
    return render(request, "inventory/product_upload.html",{'form':form})
    

def product_list(request):
    product_ = product_list.objects.all()
    return render(request, "inventory/product_list.html",{'product': product_list})
    

def product_details_view (request):
    product_ = product_details_view.objects.get(id=id)
    return render(request, "inventory/product_details.html",{'product':product_details_view})
    