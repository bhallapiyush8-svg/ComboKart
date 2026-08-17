from django.db import models
from restaurants.models import Restaurant


class FoodItem(models.Model):

    CATEGORY_CHOICES = [
        ("indian", "Indian"),
        ("fastfood", "Fast Food"),
        ("asian", "Asian"),
        ("dessert", "Dessert"),
        ("healthy", "Healthy"),
    ]

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="food_items"
    )

    name = models.CharField(max_length=150)

    description = models.TextField(blank=True)

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    image = models.URLField(blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Portion(models.Model):

    food_item = models.ForeignKey(
        FoodItem,
        on_delete=models.CASCADE,
        related_name="portions"
    )

    name = models.CharField(max_length=100)

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    description = models.CharField(
        max_length=200,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.food_item.name} - {self.name}"