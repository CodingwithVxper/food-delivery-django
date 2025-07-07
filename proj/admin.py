from django.contrib import admin
from .models import (
    Restaurant,
    Customer,
    MenuItem,
    Order,
    OrderItem,
)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.owner != request.user:
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.owner != request.user:
            return False
        return super().has_delete_permission(request, obj)


admin.site.register(Customer)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
