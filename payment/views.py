from django.shortcuts import render

# Create your views here.
from.forms import PaymentUploadForms
def upload_payment(request):
    form= PaymentUploadForms()
    return render(request,'inventory/payment_upload.html',{'form':form})

def customer_list(request,id):
    payment=payment.object.all()
    return render (request ,'inventory/payment_list.html',{'payment':payment})

def payment_details_view(request,id):
    payment=payment.object.get(id=id)
    return render (request ,'/payment_list.html',{'payment':payment})