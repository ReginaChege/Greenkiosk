from django.urls import path
from .views import upload_product
from .views import product_list
from .views import product_details_view 
urlpatterns =[
    path("product/upload/",upload_product ,name="upload_product"),
    path("product/list/",product_list ,name="product_list"),
    path("product/<int:id>/",product_details_view ,name="product_details_view "),

]
