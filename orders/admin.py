from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "customer_name",
        "phone",
        "status",
        "total_amount",
        "created_at",
    )

    search_fields = (
        "customer_name",
        "phone",
    )

    list_filter = (
        "status",
        "payment_method",
        "created_at",
    )

    inlines = [
        OrderItemInline,
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):

    list_display = (
        "order",
        "portion",
        "quantity",
        "price",
    )

    search_fields = (
        "order__customer_name",
        "portion__food_item__name",
    )
# Register your models here.
