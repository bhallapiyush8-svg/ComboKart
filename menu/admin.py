from django.contrib import admin
from .models import FoodItem, Portion


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "restaurant",
        "category",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "restaurant__name",
    )

    list_filter = (
        "category",
        "is_active",
        "restaurant",
    )


@admin.register(Portion)
class PortionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "food_item",
        "price",
        "is_active",
    )

    search_fields = (
        "name",
        "food_item__name",
    )

    list_filter = (
        "is_active",
    )