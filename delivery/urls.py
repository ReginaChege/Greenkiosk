from django.urls import path
from .views import upload_delivery
from .views import delivery_list
from .views import delivery_details_view 
urlpatterns =[
    path("delivery/upload/",upload_delivery ,name="upload_delivery"),
    path("delivery/list/",delivery_list ,name="delivery_list "),
    path("delivery/<int:id>/",delivery_details_view ,name="delivery_details_view "),

]
