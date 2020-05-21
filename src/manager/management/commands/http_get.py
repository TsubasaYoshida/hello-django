import requests
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        url = 'https://example.com/'
        response = requests.get(url)
        print(response)
