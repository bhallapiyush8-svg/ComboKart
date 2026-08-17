import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from restaurants.models import Restaurant
from menu.models import FoodItem, Portion


MENU = [
    {
        "restaurant": "Burger House",
        "food": "Mini Classic Burger",
        "category": "fastfood",
        "description": "A smaller portion classic burger.",
        "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=700&q=85",
        "portion_name": "MINI",
        "price": "89.00",
        "portion_description": "Smaller portion",
    },
    {
        "restaurant": "Spice Kitchen",
        "food": "Mini Chicken Biryani",
        "category": "indian",
        "description": "Aromatic biryani in a smaller serving.",
        "image": "https://images.unsplash.com/photo-1563379091339-03246963d96c?auto=format&fit=crop&w=700&q=85",
        "portion_name": "MINI",
        "price": "119.00",
        "portion_description": "Small serving",
    },
    {
        "restaurant": "Momo Junction",
        "food": "6 Pc Chicken Momos",
        "category": "asian",
        "description": "Juicy steamed chicken momos.",
        "image": "https://images.unsplash.com/photo-1625220194771-7ebdea0b70b9?auto=format&fit=crop&w=700&q=85",
        "portion_name": "6 PIECE",
        "price": "99.00",
        "portion_description": "Six pieces",
    },
    {
        "restaurant": "Pizza Corner",
        "food": "Mini Margherita Pizza",
        "category": "fastfood",
        "description": "Mini pizza with tomato and mozzarella.",
        "image": "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?auto=format&fit=crop&w=700&q=85",
        "portion_name": "MINI",
        "price": "109.00",
        "portion_description": "Small pizza",
    },
    {
        "restaurant": "Sweet Tooth",
        "food": "Mini Chocolate Dessert",
        "category": "dessert",
        "description": "Sweet chocolate dessert to finish your meal.",
        "image": "https://images.unsplash.com/photo-1551024506-0bccd828d307?auto=format&fit=crop&w=700&q=85",
        "portion_name": "MINI",
        "price": "79.00",
        "portion_description": "Small serving",
    },
    {
        "restaurant": "Green Bowl",
        "food": "Fresh Green Bowl",
        "category": "healthy",
        "description": "Fresh vegetables and healthy toppings.",
        "image": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=700&q=85",
        "portion_name": "REGULAR",
        "price": "99.00",
        "portion_description": "Regular serving",
    },
]

for item in MENU:
    restaurant, _ = Restaurant.objects.get_or_create(
        name=item["restaurant"],
        defaults={"is_active": True},
    )

    food, _ = FoodItem.objects.get_or_create(
        restaurant=restaurant,
        name=item["food"],
        defaults={
            "description": item["description"],
            "category": item["category"],
            "image": item["image"],
            "is_active": True,
        },
    )

    # Update existing records if they were already created.
    food.description = item["description"]
    food.category = item["category"]
    food.image = item["image"]
    food.is_active = True
    food.save()

    Portion.objects.get_or_create(
        food_item=food,
        name=item["portion_name"],
        defaults={
            "price": item["price"],
            "description": item["portion_description"],
            "is_active": True,
        },
    )

    print(f"OK: {food.name} -> {item['restaurant']}")

print("\nComboKart menu restored.")
print("Refresh /api/menu/foods/ and your website.")