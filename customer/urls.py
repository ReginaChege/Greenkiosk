from django.urls import path
from .views import upload_customer
from .views import customer_list
from .views import customer_details_view 
urlpatterns =[
    path("product/upload/",upload_customer ,name="upload_customer"),
    path("product/list/",customer_list ,name="customer_list "),
    path("product/<int:id>/",customer_details_view ,name="customer_details_view "),

]
