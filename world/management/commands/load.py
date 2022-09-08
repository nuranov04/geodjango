from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Телеграм бот'

    def handle(self, *args, **options):
        from world.load import run
        run()
