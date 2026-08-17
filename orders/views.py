from decimal import Decimal
import json

from django.db import transaction
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from menu.models import Portion
from .models import Order, OrderItem


@csrf_exempt
def create_order(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "POST method required."},
            status=405
        )

    try:
        data = json.loads(request.body)

        customer_name = str(
            data.get("customer_name", "")
        ).strip()

        phone = str(
            data.get("phone", "")
        ).strip()

        address = str(
            data.get("address", "")
        ).strip()

        payment_method = str(
            data.get("payment_method", "")
        ).strip()

        items = data.get("items", [])

        if not customer_name:
            return JsonResponse(
                {"error": "Customer name is required."},
                status=400
            )

        if not phone:
            return JsonResponse(
                {"error": "Phone number is required."},
                status=400
            )

        if not address:
            return JsonResponse(
                {"error": "Delivery address is required."},
                status=400
            )

        if not payment_method:
            return JsonResponse(
                {"error": "Payment method is required."},
                status=400
            )

        if not isinstance(items, list) or not items:
            return JsonResponse(
                {"error": "Your cart is empty."},
                status=400
            )

        with transaction.atomic():

            order = Order.objects.create(
                customer_name=customer_name,
                phone=phone,
                address=address,
                payment_method=payment_method,
                status="pending",
                total_amount=Decimal("0.00")
            )

            total_amount = Decimal("0.00")

            for item in items:

                portion_id = item.get("portionId")
                quantity = int(item.get("quantity", 1))

                if not portion_id:
                    raise ValueError(
                        "A cart item is missing its portion ID."
                    )

                if quantity < 1:
                    raise ValueError(
                        "Quantity must be at least 1."
                    )

                try:
                    portion = Portion.objects.select_related(
                        "food_item"
                    ).get(
                        id=portion_id,
                        is_active=True,
                        food_item__is_active=True
                    )

                except Portion.DoesNotExist:
                    raise ValueError(
                        f"Portion {portion_id} is no longer available."
                    )

                # Always use the price stored in Django.
                price = portion.price

                item_total = price * quantity
                total_amount += item_total

                OrderItem.objects.create(
                    order=order,
                    portion=portion,
                    quantity=quantity,
                    price=price
                )

            order.total_amount = total_amount
            order.save(update_fields=["total_amount"])

        return JsonResponse(
            {
                "success": True,
                "order_id": order.id,
                "customer_name": order.customer_name,
                "status": order.status,
                "total_amount": str(order.total_amount),
                "created_at": order.created_at.isoformat(),
                "message": "Order placed successfully!"
            },
            status=201
        )

    except ValueError as error:

        return JsonResponse(
            {"error": str(error)},
            status=400
        )

    except json.JSONDecodeError:

        return JsonResponse(
            {"error": "Invalid JSON data."},
            status=400
        )

    except Exception as error:

        return JsonResponse(
            {
                "error": "Something went wrong while creating the order.",
                "details": str(error)
            },
            status=500
        )


# ==========================================================
# ORDER TRACKING
# ==========================================================

def order_status(request, order_id):

    if request.method != "GET":
        return JsonResponse(
            {"error": "GET method required."},
            status=405
        )

    try:
        order = Order.objects.get(id=order_id)

    except Order.DoesNotExist:
        return JsonResponse(
            {
                "success": False,
                "error": "Order not found."
            },
            status=404
        )

    return JsonResponse(
        {
            "success": True,
            "order_id": order.id,
            "customer_name": order.customer_name,
            "status": order.status,
            "total_amount": str(order.total_amount),
            "created_at": order.created_at.isoformat()
        }
    )