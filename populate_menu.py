import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from restaurants.models import Restaurant
from menu.models import FoodItem, Portion


MENU = {
    "spice kitchen": [
        {
            "name": "Mini Chicken Biryani",
            "category": "indian",
            "description": "Aromatic chicken biryani with fragrant rice and spices.",
            "image": "https://images.unsplash.com/photo-1563379091339-03246963d96c?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("MINI", 119, "Small serving"),
                ("MEDIUM", 199, "Medium serving"),
                ("LARGE", 299, "Large serving"),
            ],
        },
        {
            "name": "Butter Chicken",
            "category": "indian",
            "description": "Creamy tomato-based chicken curry.",
            "image": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("SMALL", 149, "Small serving"),
                ("MEDIUM", 249, "Medium serving"),
            ],
        },
        {
            "name": "Paneer Tikka",
            "category": "indian",
            "description": "Grilled paneer marinated with Indian spices.",
            "image": "https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("6 PIECE", 129, "Six pieces"),
                ("10 PIECE", 189, "Ten pieces"),
            ],
        },
        {
            "name": "Dal Makhani",
            "category": "indian",
            "description": "Slow-cooked black lentils with butter and cream.",
            "image": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("SMALL", 99, "Small serving"),
                ("REGULAR", 159, "Regular serving"),
            ],
        },
        {
            "name": "Garlic Naan",
            "category": "indian",
            "description": "Soft naan topped with garlic and butter.",
            "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("1 PIECE", 49, "One naan"),
                ("2 PIECE", 89, "Two naan"),
            ],
        },
    ],

    "burger house": [
        {
            "name": "Mini Classic Burger",
            "category": "fastfood",
            "description": "Classic burger with fresh vegetables and sauce.",
            "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("MINI", 89, "Smaller portion"),
                ("REGULAR", 149, "Regular burger"),
            ],
        },
        {
            "name": "Chicken Cheese Burger",
            "category": "fastfood",
            "description": "Juicy chicken patty with melted cheese.",
            "image": "https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("MINI", 109, "Smaller portion"),
                ("REGULAR", 179, "Regular burger"),
            ],
        },
        {
            "name": "Crispy Chicken Burger",
            "category": "fastfood",
            "description": "Crispy chicken fillet with fresh lettuce and sauce.",
            "image": "https://images.unsplash.com/photo-1606755962773-d324e0a13086?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("MINI", 119, "Smaller portion"),
                ("REGULAR", 189, "Regular burger"),
            ],
        },
        {
            "name": "French Fries",
            "category": "fastfood",
            "description": "Crispy golden fries.",
            "image": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("SMALL", 59, "Small fries"),
                ("LARGE", 99, "Large fries"),
            ],
        },
    ],

    "momo junction": [
        {
            "name": "Chicken Momos",
            "category": "asian",
            "description": "Juicy steamed chicken momos.",
            "image": "https://images.unsplash.com/photo-1625220194771-7ebdea0b70b9?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("6 PIECE", 99, "Six pieces"),
                ("10 PIECE", 149, "Ten pieces"),
            ],
        },
        {
            "name": "Paneer Momos",
            "category": "asian",
            "description": "Steamed momos filled with spiced paneer.",
            "image": "https://images.unsplash.com/photo-1626776876729-bab4369a5a5a?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("6 PIECE", 89, "Six pieces"),
                ("10 PIECE", 139, "Ten pieces"),
            ],
        },
        {
            "name": "Fried Chicken Momos",
            "category": "asian",
            "description": "Crispy fried chicken momos.",
            "image": "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("6 PIECE", 109, "Six pieces"),
                ("10 PIECE", 159, "Ten pieces"),
            ],
        },
        {
            "name": "Schezwan Momos",
            "category": "asian",
            "description": "Spicy momos tossed in Schezwan sauce.",
            "image": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("6 PIECE", 119, "Six pieces"),
                ("10 PIECE", 169, "Ten pieces"),
            ],
        },
    ],

    "pizza corner": [
        {
            "name": "Mini Margherita Pizza",
            "category": "fastfood",
            "description": "Classic pizza with tomato and mozzarella.",
            "image": "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("MINI", 109, "Small pizza"),
                ("REGULAR", 199, "Regular pizza"),
            ],
        },
        {
            "name": "Chicken Pizza",
            "category": "fastfood",
            "description": "Pizza topped with seasoned chicken and cheese.",
            "image": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("MINI", 139, "Small pizza"),
                ("REGULAR", 249, "Regular pizza"),
            ],
        },
        {
            "name": "Farmhouse Pizza",
            "category": "fastfood",
            "description": "Loaded with fresh vegetables and cheese.",
            "image": "https://images.unsplash.com/photo-1593560708920-61dd98c46a4e?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("MINI", 129, "Small pizza"),
                ("REGULAR", 229, "Regular pizza"),
            ],
        },
        {
            "name": "Garlic Bread",
            "category": "fastfood",
            "description": "Crispy garlic bread with herbs.",
            "image": "https://images.unsplash.com/photo-1573140247632-f8fd74997d5c?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("4 PIECE", 79, "Four pieces"),
                ("6 PIECE", 109, "Six pieces"),
            ],
        },
    ],

    "sweet tooth": [
        {
            "name": "Mini Chocolate Dessert",
            "category": "dessert",
            "description": "Rich chocolate dessert.",
            "image": "https://images.unsplash.com/photo-1551024506-0bccd828d307?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("MINI", 79, "Small serving"),
                ("REGULAR", 129, "Regular serving"),
            ],
        },
        {
            "name": "Chocolate Brownie",
            "category": "dessert",
            "description": "Soft and fudgy chocolate brownie.",
            "image": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("1 PIECE", 69, "One brownie"),
                ("2 PIECE", 119, "Two brownies"),
            ],
        },
        {
            "name": "Chocolate Cake",
            "category": "dessert",
            "description": "Rich chocolate cake.",
            "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("SLICE", 89, "One slice"),
                ("LARGE SLICE", 129, "Large slice"),
            ],
        },
        {
            "name": "Gulab Jamun",
            "category": "dessert",
            "description": "Soft milk dumplings soaked in sweet syrup.",
            "image": "https://images.unsplash.com/photo-1666190094762-3f3f2d5a7f24?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("2 PIECE", 49, "Two pieces"),
                ("4 PIECE", 89, "Four pieces"),
            ],
        },
    ],

    "green bowl": [
        {
            "name": "Fresh Green Bowl",
            "category": "healthy",
            "description": "Fresh vegetables and healthy toppings.",
            "image": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("REGULAR", 99, "Regular serving"),
                ("LARGE", 149, "Large serving"),
            ],
        },
        {
            "name": "Grilled Chicken Salad",
            "category": "healthy",
            "description": "Fresh salad topped with grilled chicken.",
            "image": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("SMALL", 129, "Small serving"),
                ("REGULAR", 189, "Regular serving"),
            ],
        },
        {
            "name": "Paneer Salad Bowl",
            "category": "healthy",
            "description": "Healthy vegetable bowl with grilled paneer.",
            "image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("SMALL", 119, "Small serving"),
                ("REGULAR", 179, "Regular serving"),
            ],
        },
        {
            "name": "Fruit Bowl",
            "category": "healthy",
            "description": "Fresh seasonal fruits.",
            "image": "https://images.unsplash.com/photo-1490474418585-ba9bad8fd0ea?auto=format&fit=crop&w=700&q=85",
            "portions": [
                ("SMALL", 79, "Small bowl"),
                ("REGULAR", 119, "Regular bowl"),
            ],
        },
    ],
}


def find_restaurant(name):
    restaurants = Restaurant.objects.filter(is_active=True)

    for restaurant in restaurants:
        if restaurant.name.strip().lower() == name.strip().lower():
            return restaurant

    return None


print("\n==============================")
print(" ComboKart Menu Population")
print("==============================\n")


for restaurant_name, foods in MENU.items():

    restaurant = find_restaurant(restaurant_name)

    if not restaurant:
        print(f"SKIPPED: Restaurant not found -> {restaurant_name}")
        continue

    print(f"\nRestaurant: {restaurant.name}")

    for food_data in foods:

        food, created = FoodItem.objects.get_or_create(
            restaurant=restaurant,
            name=food_data["name"],
            defaults={
                "description": food_data["description"],
                "category": food_data["category"],
                "image": food_data["image"],
                "is_active": True,
            }
        )

        # Update existing food item too
        food.description = food_data["description"]
        food.category = food_data["category"]
        food.image = food_data["image"]
        food.is_active = True
        food.save()

        if created:
            print(f"  + Food: {food.name}")
        else:
            print(f"  = Food already exists: {food.name}")

        for portion_name, price, description in food_data["portions"]:

            portion, portion_created = Portion.objects.get_or_create(
                food_item=food,
                name=portion_name,
                defaults={
                    "price": price,
                    "description": description,
                    "is_active": True,
                }
            )

            portion.price = price
            portion.description = description
            portion.is_active = True
            portion.save()

            if portion_created:
                print(f"      + Portion: {portion_name} ₹{price}")
            else:
                print(f"      = Portion exists: {portion_name} ₹{price}")


print("\n==============================")
print(" MENU POPULATION COMPLETE")
print("==============================\n")