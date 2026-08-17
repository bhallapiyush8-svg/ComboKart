from django.http import JsonResponse

from .models import FoodItem


def food_list(request):

    foods = (
        FoodItem.objects
        .filter(is_active=True)
        .select_related("restaurant")
        .prefetch_related("portions")
    )

    # Optional restaurant filter
    restaurant_id = request.GET.get("restaurant")

    if restaurant_id:

        try:
            restaurant_id = int(restaurant_id)

            foods = foods.filter(
                restaurant_id=restaurant_id
            )

        except ValueError:

            return JsonResponse(
                {
                    "error":
                    "Invalid restaurant ID."
                },
                status=400
            )

    data = []

    for food in foods:

        data.append({

            "id":
                food.id,

            "name":
                food.name,

            "restaurant_id":
                food.restaurant.id,

            "restaurant":
                food.restaurant.name,

            "category":
                food.get_category_display(),

            "description":
                food.description,

            "image":
                food.image,

            "portions": [

                {
                    "id":
                        portion.id,

                    "name":
                        portion.name,

                    "price":
                        str(portion.price),

                    "description":
                        portion.description,

                }

                for portion in food.portions.filter(
                    is_active=True
                )

            ],

        })

    return JsonResponse(
        data,
        safe=False
    )