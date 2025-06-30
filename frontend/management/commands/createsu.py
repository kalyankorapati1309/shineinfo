from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates a superuser if it doesn’t exist'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = 'kalyan'
        password = 'Samgrace@1309'  # Change this to your secure password
        email = 'kalyankorapati1309@gmail.com'

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS('Superuser created.'))
        else:
            self.stdout.write('Superuser already exists.')
