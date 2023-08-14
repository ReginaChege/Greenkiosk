from django.urls import path
from .views import cart_customer
from .views import cart_list
from .views import cart_details_view 
urlpatterns =[
    path("cart/upload/",cart_customer ,name="upload_cart"),
    path("cart/list/",cart_list ,name="cart_list "),
    path("cart/<int:id>/",cart_details_view ,name="cart_details_view "),

]
