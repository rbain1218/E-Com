====================================
E-COM DJANGO E-COMMERCE PROJECT
====================================

ABOUT PROJECT
------------------------------------
E-Com is a Django-based e-commerce website where users can browse products,
add them to their cart, and purchase them. It also includes an admin dashboard 
for superusers to view all users, products, and cart data in one place.

This project is ideal for university submissions or as a learning project 
for Django web development.

------------------------------------
FEATURES
------------------------------------
✔ User registration and login system  
✔ Product listing and details page  
✔ Add to cart and checkout system  
✔ Chat module (for future use)  
✔ Seller management module  
✔ Admin dashboard for viewing:
   - All users
   - All products
   - All cart items  
✔ PostgreSQL database support  
✔ Bootstrap 5 responsive frontend design  

------------------------------------
TECHNOLOGIES USED
------------------------------------
- Python 3.13
- Django 4.2
- PostgreSQL (Database)
- Bootstrap 5 (Frontend)
- HTML, CSS, JavaScript
- Crispy Forms
- Django REST Framework (optional future APIs)

------------------------------------
PROJECT STRUCTURE
------------------------------------
ECom/
│
├── accounts/        → Handles login, registration, logout
├── cart/            → Handles shopping cart
├── chat/            → Chat module (optional)
├── dashboard/       → Admin dashboard (superuser only)
├── products/        → Product display and home page
├── seller/          → Seller management
├── static/          → CSS, JS, images
├── templates/       → Common HTML templates
└── manage.py        → Django project manager

------------------------------------
DATABASE CONFIGURATION
------------------------------------
This project uses PostgreSQL by default.

1️⃣ Create a PostgreSQL database:
    CREATE DATABASE ecomdb;
    CREATE USER ecomdb WITH PASSWORD 'yourpassword';
    GRANT ALL PRIVILEGES ON DATABASE ecomdb TO ecomdb;

2️⃣ Update your DATABASES setting in ECom/settings.py:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'ecomdb',
            'USER': 'ecomdb',
            'PASSWORD': 'yourpassword',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

------------------------------------
INSTALLATION & SETUP
------------------------------------
1️⃣ Create and activate virtual environment:
    python3 -m venv venv
    source venv/bin/activate     (Mac/Linux)
    venv\Scripts\activate        (Windows)

2️⃣ Install dependencies:
    pip install -r requirements.txt

3️⃣ Run migrations:
    python manage.py makemigrations
    python manage.py migrate

4️⃣ Create superuser:
    python manage.py createsuperuser

5️⃣ Run server:
    python manage.py runserver

6️⃣ Open browser:
    http://127.0.0.1:8000/

------------------------------------
ADMIN DASHBOARD
------------------------------------
Superusers can access the admin dashboard at:
    http://127.0.0.1:8000/dashboard/

- Shows list of all users, products, and cart items.
- Accessible only to users with superuser privileges.

------------------------------------
DEFAULT ROUTES
------------------------------------
/                  → Home Page (Products)
/accounts/login/   → Login Page
/accounts/register/→ User Registration
/accounts/logout/  → Logout
/cart/             → Cart Page
/seller/           → Seller Page
/chat/             → Chat Page
/dashboard/        → Admin Dashboard (superuser only)

------------------------------------
HOW TO LOGIN AS ADMIN
------------------------------------
1️⃣ Go to: http://127.0.0.1:8000/accounts/login/
2️⃣ Use your superuser credentials.
3️⃣ If you’re superuser → Redirected to Admin Dashboard
4️⃣ If normal user → Redirected to Home page

------------------------------------
CREDITS
------------------------------------
Developer: Rahul Bain  
Language: Python Django  
Email: rbain1218@gmail.com  
GitHub: https://github.com/rbain1218

------------------------------------
LICENSE
------------------------------------
This project is open-source and can be used for educational 
or academic purposes with proper credit.
