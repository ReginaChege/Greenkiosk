from django.shortcuts import render

# Create your views here.
from.forms import CustomerUploadForms
def upload_customer(request):
    form=CustomerUploadForms()
    return render(request,'inventory/customer_upload.html',{'form':form})

def customer_list(request,id):
    customer=customer.object.all()
    return render (request ,'inventory/customer_list.html',{'customer':customer})

def customer_details_view(request,id):
    customer=customer.object.get(id=id)
    return render (request ,'/customer_list.html',{'customer':customer})