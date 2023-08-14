from django.shortcuts import render

# Create your views here.
from.forms import ShipmentUploadForms
def upload_shipment(request):
    form=ShipmentUploadForms()
    return render(request,'inventory/shipment_upload.html',{'form':form})

def shipment_list(request,id):
   shipment=shipment.object.all()
   return render (request ,'inventory/shipment_list.html',{'shipment':shipment})

def shipment_details_view(request,id):
    shipment=shipment.object.get(id=id)
    return render (request ,'/shipment_list.html',{'shipment':shipment})


