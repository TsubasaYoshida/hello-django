from django.core.management.base import BaseCommand

from ...models import Brand


class Command(BaseCommand):
    def handle(self, *args, **options):
        Brand.objects.create(code="006", name="ナンバーシックス")
