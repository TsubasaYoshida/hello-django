import requests
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
        params = {'city': 130010}
        response = requests.get(url, params=params)

        # あまりいけてない
        print(response.status_code == 200)
        print(response.headers['Content-Type'] == 'application/json; charset=utf-8')
