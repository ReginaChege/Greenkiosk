from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display=("customer_id","email","first_name","second_name")

admin.site.register(Customer,CustomerAdmin)

# Register your models here.
