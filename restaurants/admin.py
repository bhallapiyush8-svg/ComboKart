from django.contrib import admin
from .models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "phone",
    )

    list_filter = (
        "is_active",
    )