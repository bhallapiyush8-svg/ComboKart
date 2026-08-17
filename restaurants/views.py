import math

from django.http import JsonResponse

from .models import Restaurant


def calculate_distance(
    latitude1,
    longitude1,
    latitude2,
    longitude2
):
    """
    Calculate distance between two coordinates
    using the Haversine formula.

    Returns distance in kilometres.
    """

    earth_radius_km = 6371

    lat1 = math.radians(latitude1)
    lat2 = math.radians(latitude2)

    lat_difference = math.radians(
        latitude2 - latitude1
    )

    lon_difference = math.radians(
        longitude2 - longitude1
    )

    a = (
        math.sin(lat_difference / 2) ** 2
        +
        math.cos(lat1)
        * math.cos(lat2)
        * math.sin(lon_difference / 2) ** 2
    )

    c = 2 * math.atan2(
        math.sqrt(a),
        math.sqrt(1 - a)
    )

    return earth_radius_km * c


def restaurant_list(request):

    restaurants = Restaurant.objects.filter(
        is_active=True
    )

    # User location from query parameters
    latitude = request.GET.get("latitude")
    longitude = request.GET.get("longitude")

    data = []

    for restaurant in restaurants:

        # Skip restaurants without coordinates
        if (
            restaurant.latitude is None
            or restaurant.longitude is None
        ):
            continue

        restaurant_latitude = float(
            restaurant.latitude
        )

        restaurant_longitude = float(
            restaurant.longitude
        )

        # If user location was provided,
        # calculate distance.
        if latitude and longitude:

            try:

                user_latitude = float(latitude)
                user_longitude = float(longitude)

                distance = calculate_distance(
                    user_latitude,
                    user_longitude,
                    restaurant_latitude,
                    restaurant_longitude
                )

            except ValueError:

                return JsonResponse(
                    {
                        "error":
                        "Invalid latitude or longitude."
                    },
                    status=400
                )

            # Only restaurants within 5 km
            if distance > 5:
                continue

        else:

            distance = None

        data.append({

            "id":
                restaurant.id,

            "name":
                restaurant.name,

            "description":
                restaurant.description,

            "phone":
                restaurant.phone,

            "address":
                restaurant.address,

            "latitude":
                restaurant_latitude,

            "longitude":
                restaurant_longitude,

            "image":
                restaurant.image,

            "distance_km":
                round(distance, 2)
                if distance is not None
                else None,
        })

    # Closest restaurants first
    data.sort(
        key=lambda restaurant:
        restaurant["distance_km"]
        if restaurant["distance_km"] is not None
        else 999999
    )

    return JsonResponse(
        data,
        safe=False
    )