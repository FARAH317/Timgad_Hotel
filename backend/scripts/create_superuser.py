import os
from django.contrib.auth import get_user_model

User = get_user_model()

email = "admin@timgadhotel.com"

if not User.objects.filter(email=email).exists():
    User.objects.create_superuser(
        username="admin",
        email=email,
        password="admin123"
    )
    print("Superuser created ✅")
else:
    print("Superuser already exists ✅")