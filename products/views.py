from django.shortcuts import render

# Create your views here.
from.forms import ProductUploadForms
def upload_product(request):
    form=ProductUploadForms()
    return render(request,'product/product_upload.html',{'form':form})

def product_list(request,id):
    product=product.object.all()
    return render (request ,'inventory/product_list.html',{'product':product})

def product_details_view(request,id):
    product=product.object.get(id=id)
    return render (request ,'/product_list.html',{'product':product})