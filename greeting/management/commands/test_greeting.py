from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Test if greeting plugin is installed"

    def handle(self, *args, **options):
        
        self.stdout.write(
            self.style.SUCCESS("Successfully tested greetings plugin")
        )