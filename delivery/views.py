from django.shortcuts import render

# Create your views here.
from.form import DeliveryUploadForms
def upload_delivery(request):
    form=DeliveryUploadForms()
    return render(request,'inventory/deliveryupload.html',{'form':form})

def delivery_list(request,id):
   delivery=delivery.object.all()
   return render (request ,'inventory/delivery_list.html',{'delivery':delivery})

def delivery_details_view(request,id):
    delivery=delivery.object.get(id=id)
    return render (request ,'inventory/delivery_list.html',{'delivery':delivery})

