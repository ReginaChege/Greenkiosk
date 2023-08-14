from django.urls import path
from .views import upload_order
from .views import order_list
from .views import order_details_view 
urlpatterns =[
    path("order/upload/",upload_order ,name="upload_order"),
    path("order/list/",order_list ,name="order_list "),
    path("order/<int:id>/",order_details_view ,name="order_details_view "),

]
