from django.contrib.auth.models import User

User.objects.create_superuser(username="AdminUser", password="UnHacKabLE", email="adminuser@example.com")
