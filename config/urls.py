from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    # Django Admin
    path(
        "admin/",
        admin.site.urls
    ),

    # Food Menu API
    path(
        "api/menu/",
        include("menu.urls")
    ),

    # Orders API
    path(
        "api/orders/",
        include("orders.urls")
    ),

    # Restaurants API
    path(
        "api/restaurants/",
        include("restaurants.urls")
    ),

    # ComboKart Homepage
    path(
        "",
        TemplateView.as_view(
            template_name="index.html"
        ),
        name="home",
    ),
]