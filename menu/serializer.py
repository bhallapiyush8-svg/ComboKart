from rest_framework import serializers
from .models import FoodItem, Portion


class PortionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portion
        fields = [
            "id",
            "name",
            "price",
            "description",
            "is_active",
        ]


class FoodItemSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(
        source="restaurant.name",
        read_only=True
    )

    portions = PortionSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = FoodItem
        fields = [
            "id",
            "name",
            "description",
            "category",
            "image",
            "is_active",
            "restaurant",
            "restaurant_name",
            "portions",
        ]