from django.shortcuts import render

# Create your views here.
from.form import CartUploadForms
def upload_cart(request):
    form=CartUploadForms()
    return render(request,'inventory/cart_upload.html',{'form':form})

def cart_list(request,id):
    cart=cart_list.object.all()
    return render (request ,'inventory/cart_list.html',{'cart':cart})

def cart_details_view(request,id):
    cart=cart_details_view.object.get(id=id)
    return render (request ,'inventory/cart_list.html',{'cart':cart})