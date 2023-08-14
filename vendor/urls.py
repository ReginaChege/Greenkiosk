from django.urls import path
from .views import upload_vendor
from .views import vendor_list
from .views import vendor_details_view 
urlpatterns =[
    path("vendor/upload/",upload_vendor ,name="upload_vendor"),
    path("vendor/list/",vendor_list ,name="vendor_list "),
    path("vendor/<int:id>/",vendor_details_view ,name="vendor_details_view "),

]
