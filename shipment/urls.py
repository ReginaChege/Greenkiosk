from django.urls import path
from .views import upload_shipment
from .views import shipment_list
from .views import shipment_details_view 
urlpatterns =[
    path("shipment/upload/",upload_shipment ,name="upload_shipment"),
    path("shipment/list/",shipment_list ,name="shipment_list "),
    path("shipment/<int:id>/",shipment_details_view ,name="shipment_details_view "),

]
