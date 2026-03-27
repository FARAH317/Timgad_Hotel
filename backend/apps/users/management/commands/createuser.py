from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Create a test user'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='User email')
        parser.add_argument('password', type=str, help='User password')
        parser.add_argument('--first-name', type=str, default='Test', help='First name')
        parser.add_argument('--last-name', type=str, default='User', help='Last name')
        parser.add_argument('--role', type=str, default='CLIENT', choices=['ADMIN', 'STAFF', 'CLIENT'], help='User role')

    def handle(self, *args, **options):
        email = options['email']
        password = options['password']
        first_name = options['first_name']
        last_name = options['last_name']
        role = options['role']

        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.WARNING(f'User with email {email} already exists'))
            return

        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role=role
        )

        self.stdout.write(self.style.SUCCESS(f'Successfully created user {email}'))