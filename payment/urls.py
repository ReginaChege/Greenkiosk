from django.urls import path
from .views import upload_payment
from .views import payment_list
from .views import payment_details_view 
urlpatterns =[
    path("payment/upload/",upload_payment ,name="upload_payment"),
    path("payment/list/",payment_list ,name="payment_list "),
    path("payment/<int:id>/",payment_details_view ,name="payment_details_view "),

]
