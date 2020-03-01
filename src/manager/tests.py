from django.test import TestCase

from .models import Brand

class ManagerTest(TestCase):
    def test_create_brand(self):
        self.assertEqual(Brand.objects.count(), 0)
        Brand.create()
        print(Brand.objects.all().first())
        self.assertEqual(Brand.objects.count(), 1)
