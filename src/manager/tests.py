from django.test import TestCase

from django.core import management

from .models import Brand


class ManagerTest(TestCase):
    def test_create_brand(self):
        self.assertEqual(Brand.objects.count(), 0)
        management.call_command('receive_stock')
        print(Brand.objects.all().first())
        self.assertEqual(Brand.objects.count(), 1)
