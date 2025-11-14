# Hotel Reservation System

A full-stack **Hotel Reservation System** with a **React + Vite frontend** and a **Django REST Framework backend**.  
It allows users to browse rooms, make reservations, process payments, and receive notifications, while admins can manage all hotel operations.

---

## Project Overview

This project is designed for managing hotel operations and reservations, providing:

- **User authentication & role-based access** (Admin, Staff, Customer)
- **Room management** (CRUD for rooms, types, and amenities)
- **Reservation management** with state transitions
- **Payment processing** (Stripe, PayPal, Cash)
- **Notifications** via email and SMS
- **Admin dashboard** with analytics and reports

---

## Tech Stack

### Backend
- Django 5.x, Django REST Framework
- PostgreSQL database
- JWT Authentication
- Celery for async tasks (email/SMS)
- Python 3.12

### Frontend
- React 19.x with Vite
- Redux for state management
- Tailwind CSS for styling
- Axios for API requests
- JavaScript (ES6+)

---

## Backend Structure

\\\
backend/
├── manage.py
├── requirements.txt
├── .env
├── config/                    # Django project configuration
├── apps/                      # Django apps
│   ├── core/                  # Shared utilities
│   ├── users/                 # Users & authentication
│   ├── rooms/                 # Rooms & amenities
│   ├── reservations/          # Reservation management
│   ├── payments/              # Payment processing
│   └── notifications/         # Email/SMS notifications
├── infrastructure/            # External services
└── static/
\\\

---

## Frontend Structure

\\\
frontend/
├── public/
│   └── index.html
├── src/
│   ├── app/
│   │   ├── App.jsx
│   │   ├── store.js
│   │   └── routes.jsx
│   ├── features/             # Organized by feature
│   │   ├── auth/             # Authentication
│   │   ├── rooms/            # Room components & store
│   │   ├── reservations/     # Reservation components & store
│   │   ├── payments/         # Payment components & store
│   │   └── dashboard/        # Admin dashboard
│   ├── components/           # Reusable components
│   ├── services/             # Global API services
│   ├── utils/                # Helpers, validators
│   ├── styles/               # Tailwind CSS
│   └── assets/               # Images, icons
├── package.json
├── tailwind.config.js
├── vite.config.js
└── .env
\\\

---

## Setup Instructions

### Backend

\\\ash
# Create virtual environment
python -m venv venv

# Activate
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Migrate database
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
\\\

### Frontend

\\\ash
# Install dependencies
npm install

# Start dev server
npm run dev
\\\

---

## Environment Variables

Create .env files in both ackend/ and rontend/ with necessary secrets:

**Backend**
\\\
DEBUG=True
SECRET_KEY=<your_secret_key>
DATABASE_URL=postgres://user:password@localhost:5432/hotel_db
EMAIL_HOST=smtp.example.com
EMAIL_USER=<email>
EMAIL_PASSWORD=<password>
\\\

**Frontend**
\\\
VITE_API_URL=http://localhost:8000/api
\\\

---

## Contributing

- Fork the repository  
- Create a feature branch (\git checkout -b feature/my-feature\)  
- Commit changes (\git commit -m "Add feature"\)  
- Push branch (\git push origin feature/my-feature\)  
- Open a pull request  

---


