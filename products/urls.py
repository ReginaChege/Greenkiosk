from django.urls import path
from .views import upload_products
from .views import products_list
from .views import products_details_view 
urlpatterns =[
    path("product/upload/",upload_products ,name="upload_products"),
    path("product/list/",products_list ,name="products_list "),
    path("product/<int:id>/",products_details_view ,name="products_details_view "),

]
