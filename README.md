https://combokart.onrender.com/
# 🍽️ ComboKart — One Platter. Many Restaurants.


> **Discover nearby restaurants, choose dishes from multiple restaurants, and build one personalized platter.**

🔗 **Live Demo:** https://combokart.onrender.com

ComboKart is a full-stack Django web application that solves a simple problem: **why should you have to choose only one restaurant when you want to try several dishes?**

The platform detects the user's location, finds active restaurants within a **5 km radius**, loads their menus and portions, and lets the user combine dishes from different restaurants into a single customizable platter.

---

## ✨ Features

### 📍 Location-Based Restaurant Discovery

* Requests the user's current location through the browser.
* Uses latitude and longitude to find nearby restaurants.
* Calculates distance using the **Haversine formula**.
* Shows only restaurants within a **5 km radius**.
* Sorts restaurants by distance from the user.

### 🍔 Multi-Restaurant Menu

* Displays menus from restaurants within the user's 5 km range.
* Supports multiple food categories.
* Displays restaurant information alongside every dish.
* Supports different portions and prices for each food item.

### 🧩 Custom Combo Platter

Users can combine dishes from different restaurants into **one platter**.

Example:

```text
Spice Kitchen       → Chicken Biryani
Burger House        → Chicken Cheese Burger
Momo Junction       → Chicken Momos
Pizza Corner        → Chicken Pizza
Sweet Tooth         → Chocolate Brownie
```

All selected items can be added to one cart and ordered together.

### 🛒 Smart Cart

* Add multiple dishes at once.
* Select different portions.
* Increase/decrease quantities.
* Remove individual items.
* Cart persists using browser `localStorage`.
* Automatically calculates subtotal, delivery and total.

### 📦 Order Management

* Customer checkout form.
* Order creation through Django REST-style APIs.
* Order ID generation.
* Payment method selection.
* Persistent order status.

### 🚚 Live Order Tracking

Customers can enter their Order ID and view statuses such as:

```text
Order Placed
      ↓
Confirmed
      ↓
Preparing
      ↓
Out for Delivery
      ↓
Delivered
```

The tracking interface automatically refreshes the order status periodically.

### 📱 Responsive UI

The frontend is designed to work across:

* Desktop
* Tablet
* Mobile

---

## 🏗️ Architecture

```text
                         ┌─────────────────────┐
                         │      User Browser    │
                         │   ComboKart Frontend │
                         └──────────┬──────────┘
                                    │
                  ┌─────────────────┼─────────────────┐
                  │                 │                 │
                  ▼                 ▼                 ▼
           Location API        Menu API          Orders API
                  │                 │                 │
                  ▼                 ▼                 ▼
         /api/restaurants/   /api/menu/foods/   /api/orders/
                  │
                  ▼
          Haversine Distance
                  │
                  ▼
        Restaurants within 5 km
                  │
                  ▼
           Restaurant Menus
                  │
                  ▼
          Custom Combo Platter
                  │
                  ▼
              Checkout
```

---

## 🛠️ Tech Stack

### Backend

* **Python**
* **Django**
* **Django REST Framework**
* **SQLite** for local development
* **PostgreSQL-ready configuration** for production
* **Gunicorn**

### Frontend

* HTML5
* CSS3
* JavaScript
* Browser Geolocation API
* Fetch API
* LocalStorage

### Deployment

* **Render**
* GitHub
* Automatic deployment from the `main` branch

---

## 📂 Project Structure

```text
ComboKart/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── restaurants/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── menu/
│   ├── models.py
│   ├── views.py
│   ├── serializer.py
│   ├── urls.py
│   └── migrations/
│
├── orders/
│   ├── models.py
│   ├── views.py
│   └── migrations/
│
├── users/
│
├── frontend/
│   └── index.html
│
├── populate_menu.py
├── populate_restaurants.py
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🔑 Core API Endpoints

### Restaurants

```http
GET /api/restaurants/
```

Returns all active restaurants.

For location-based discovery:

```http
GET /api/restaurants/?latitude=28.45358&longitude=77.05720
```

The endpoint calculates the distance between the user and each restaurant and returns only restaurants within **5 km**.

Example:

```json
{
    "id": 1,
    "name": "spice kitchen",
    "latitude": 28.45358,
    "longitude": 77.05720,
    "distance_km": 0.01
}
```

---

### Menu

```http
GET /api/menu/foods/
```

Get active menu items.

To get a specific restaurant's menu:

```http
GET /api/menu/foods/?restaurant=1
```

Menu items include:

* Food name
* Restaurant
* Category
* Description
* Image
* Portions
* Prices

---

### Create Order

```http
POST /api/orders/create/
```

Example request:

```json
{
    "customer_name": "John",
    "phone": "9876543210",
    "address": "New Delhi, India",
    "payment_method": "UPI",
    "items": [
        {
            "portionId": 1,
            "quantity": 2
        },
        {
            "portionId": 7,
            "quantity": 1
        }
    ]
}
```

---

### Track Order

```http
GET /api/orders/<order_id>/
```

Returns the current order status and details.

---

## 📏 How the 5 KM Radius Works

ComboKart uses the **Haversine formula** to calculate the great-circle distance between two geographic coordinates.

```text
User Location
     │
     ▼
Latitude + Longitude
     │
     ▼
Calculate distance to each restaurant
     │
     ▼
distance <= 5 km ?
     │
   ┌─┴─┐
  YES  NO
   │    │
   ▼    ▼
Show   Hide
```

This allows the restaurant discovery system to work dynamically based on the user's actual location instead of relying on a fixed list.

---

## 🚀 Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/bhallapiyush8-svg/ComboKart.git
cd ComboKart
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Populate restaurants

```bash
python populate_restaurants.py
```

### 6. Populate menus

```bash
python populate_menu.py
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 🌍 Deployment

ComboKart is deployed using **Render** with automatic deployment from GitHub.

Production URL:

```text
https://combokart.onrender.com
```

The deployment process runs database migrations and seed scripts before collecting static files.

---

## 🧠 What I Learned Building This

This project helped me work with:

* Django project architecture
* Django models and relationships
* REST-style API development
* Django ORM
* Nested menu/portion data
* Geographic distance calculations
* Browser Geolocation API
* Asynchronous JavaScript and `fetch()`
* Dynamic DOM rendering
* LocalStorage-based state management
* Order and cart workflows
* Production deployment with Render
* Git and GitHub workflows
* Environment-based Django configuration

---

## 🔮 Future Improvements

Some planned improvements include:

* 💳 Real payment gateway integration
* 🗺️ Interactive restaurant map
* 🔐 User authentication and profiles
* ⭐ Restaurant and food ratings
* ❤️ Favourite restaurants and dishes
* 🔔 Real-time order notifications
* 🚚 Delivery partner tracking
* 📊 Restaurant analytics dashboard
* 🗄️ Production PostgreSQL database
* 🤖 Personalized food recommendations
* 💰 Dynamic delivery pricing based on distance

---

## 🎯 Why ComboKart?

Traditional food-ordering platforms generally make the user choose a restaurant first.

ComboKart flips that concept:

```text
Traditional:

Restaurant
    ↓
Choose Food
    ↓
Order


ComboKart:

Your Location
    ↓
Nearby Restaurants
    ↓
Choose Anything
    ↓
Mix Multiple Restaurants
    ↓
One Personalized Platter
```

The goal is to make **food variety** the starting point rather than the restaurant.

---

## 👨‍💻 Developer

**Piyush Bhalla**, **Sarthak Kohli**

Built as a full-stack Django project focused on location-based restaurant discovery and multi-restaurant food combinations.

---

## 📄 License

This project is currently intended for educational and portfolio purposes.

---

⭐ **If you found ComboKart interesting, consider giving the repository a star!**
