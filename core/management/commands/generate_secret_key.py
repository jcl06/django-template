from django.core.management import BaseCommand
from configs.generate_secret_key import generate_secret_key

class Command(BaseCommand):
    # Show this when the user types help
    help = "Generate Secret Key"
    def handle(self, *args, **options):
        return generate_secret_key()