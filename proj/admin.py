from django.contrib import admin
from .models import (
    Restaurant,
    Customer,
    MenuItem,
    Order,
    OrderItem,
)

admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
