# E-Commerce Backend + Frontend

Simple e-commerce project built with Django, Django REST Framework, and React.

## Features

- User registration & login (JWT auth)
- Product listing
- Add to cart
- Update cart / remove items
- Checkout (create orders)
- Order history
- Stock management (auto decrease on order)
- Basic payment flow (mock / simple)

## Tech Stack

- Backend: Django + DRF
- Frontend: React (CDN, class components)
- Database: PostgreSQL (or SQLite for dev)

## Project Structure

```
backend/
  products/
  users/
  cart/
  orders/

frontend/
  index.html
  app.js
```

## Setup (Backend)

```bash
git clone <repo>
cd backend

python -m venv venv
venv\Scripts\activate  # Windows

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

## Setup (Frontend)

Just open the HTML file:

```
ecom_frontend/index.html
```

(make sure backend is running)

## Basic Flow

1. User registers / logs in
2. Fetch products
3. Add items to cart
4. View cart
5. Checkout → creates order + clears cart
6. Stock is reduced

## Notes

- JWT token must be sent in headers:

```
Authorization: Bearer <token>
```

- Make sure migrations are run before using orders (common error if not)

## Future Improvements

- Real payment integration (Stripe, etc)
- Better UI (proper React app instead of CDN)
- Product search & filters
- Admin dashboard
