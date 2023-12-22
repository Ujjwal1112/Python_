from django.contrib import admin
from orders.models import Orders

# Register your models here.


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ("tracking_id", "address", "mobile_number", "status", "order_total","created_at")
    list_filter = ("status",)
    sortable_by = ("order_total",)