from django.shortcuts import render

# Create your views here.
from.forms import OrderUploadForms
def upload_order(request):
    form=OrderUploadForms()
    return render(request,'inventory/order_upload.html',{'form':form})

def order_list(request,id):
    order=order.object.all()
    return render (request ,'inventory/order_list.html',{'order':order})

def order_details_view(request,id):
    order=order.object.get(id=id)
    return render (request ,'/order_list.html',{'order':order})