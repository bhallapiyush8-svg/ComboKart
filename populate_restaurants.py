import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from restaurants.models import Restaurant


RESTAURANTS = [
    {
        "name": "spice kitchen",
        "description": "INDIAN FOOD AND BIRYANI SPECIALIST",
        "phone": "7011802582",
        "address": "New Delhi, India",
        "latitude": 28.453580,
        "longitude": 77.057200,
        "image": "",
    },
    {
        "name": "Burger House",
        "description": "",
        "phone": "",
        "address": "",
        "latitude": 28.453500,
        "longitude": 77.057000,
        "image": "",
    },
    {
        "name": "Spice Kitchen",
        "description": "",
        "phone": "",
        "address": "",
        "latitude": 28.453000,
        "longitude": 77.057000,
        "image": "",
    },
    {
        "name": "Momo Junction",
        "description": "",
        "phone": "",
        "address": "",
        "latitude": 28.453000,
        "longitude": 77.057000,
        "image": "",
    },
    {
        "name": "Pizza Corner",
        "description": "",
        "phone": "",
        "address": "",
        "latitude": 28.453500,
        "longitude": 77.057000,
        "image": "",
    },
    {
        "name": "Sweet Tooth",
        "description": "the best sweet and bakery restuarant",
        "phone": "",
        "address": "",
        "latitude": 28.453000,
        "longitude": 77.050000,
        "image": "",
    },
    {
        "name": "Green Bowl",
        "description": "the best restuarant for healthy salads and food",
        "phone": "",
        "address": "aa",
        "latitude": 28.453000,
        "longitude": 77.050000,
        "image": "",
    },
]


print("\n==============================")
print(" ComboKart Restaurant Population")
print("==============================\n")


for data in RESTAURANTS:

    restaurant, created = Restaurant.objects.update_or_create(
        name=data["name"],
        defaults={
            "description": data["description"],
            "phone": data["phone"],
            "address": data["address"],
            "latitude": data["latitude"],
            "longitude": data["longitude"],
            "image": data["image"],
            "is_active": True,
        },
    )

    if created:
        print(f"+ Created: {restaurant.name}")
    else:
        print(f"= Updated: {restaurant.name}")


print("\n==============================")
print(" RESTAURANT POPULATION COMPLETE")
print("==============================\n")