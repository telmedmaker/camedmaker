from django.core.management.base import BaseCommand

from recipes.tasks import process_recipe_requests


class Command(BaseCommand):
    help = "Process recipe requests"

    def handle(self, *args, **options):
        process_recipe_requests()
