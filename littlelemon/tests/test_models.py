from django.test import TestCase
from restaurant.models import Menu, Booking
from decimal import Decimal
from datetime import datetime


class MenuTest(TestCase):

    def test_create_item(self):
        item = Menu.objects.create(title="IceCream", price=Decimal('80'), inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

    def test_default_inventory(self):
        item = Menu.objects.create(title="Cake", price=Decimal('50'))
        self.assertEqual(item.inventory, 5)


class BookingTest(TestCase):

    def test_create_booking(self):
        booking = Booking.objects.create(
            name="John Doe",
            number_of_guests=4,
            booking_date=datetime(2024, 3, 16, 15, 0)
        )
        expected_str = "TJohn Doe for 4 guests on 2024-03-16 15:00:00"
        self.assertEqual(str(booking), expected_str)

    def test_default_number_of_guests(self):
        booking = Booking.objects.create(
            name="Jane Doe",
            booking_date=datetime(2024, 4, 1, 19, 0)
        )
        self.assertEqual(booking.number_of_guests, 6)