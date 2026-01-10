"""
Test cases for booking views and APIs
"""
from django.test import TestCase, Client
from django.urls import reverse
from datetime import date
import json
from .models import Booking
from .forms import BookingForm


class BookingViewTest(TestCase):
    """Test cases for Booking views"""

    def setUp(self):
        """Set up test client and test data"""
        self.client = Client()
        self.valid_booking_data = {
            'name': 'Test User',
            'phone': '+1122334455',
            'date': date(2026, 1, 19),  # Monday
            'level': 'beginner',
        }

    def test_index_view(self):
        """Test the index/home page loads"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_book_view_get(self):
        """Test GET request to book view"""
        response = self.client.get(reverse('book'))
        self.assertEqual(response.status_code, 200)

    def test_book_view_post_valid(self):
        """Test POST request with valid booking data"""
        response = self.client.post(reverse('book'), data=self.valid_booking_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Booking.objects.count(), 1)
        booking = Booking.objects.first()
        self.assertEqual(booking.name, 'Test User')

    def test_book_view_post_invalid(self):
        """Test POST request with invalid data"""
        invalid_data = self.valid_booking_data.copy()
        invalid_data['date'] = date(2025, 1, 1)  # Invalid year
        response = self.client.post(reverse('book'), data=invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Booking.objects.count(), 0)

    def test_my_bookings_view(self):
        """Test my bookings view loads"""
        response = self.client.get(reverse('my_bookings'))
        self.assertEqual(response.status_code, 200)

    def test_search_booking_found(self):
        """Test searching for an existing booking"""
        booking = Booking.objects.create(**self.valid_booking_data)
        response = self.client.get(
            reverse('search_booking'),
            {'name': 'Test User', 'phone': '+1122334455'}
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['status'], 'found')
        self.assertEqual(len(data['bookings']), 1)

    def test_search_booking_not_found(self):
        """Test searching for non-existent booking"""
        response = self.client.get(
            reverse('search_booking'),
            {'name': 'Unknown', 'phone': '+9999999999'}
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['status'], 'not_found')

    def test_cancel_booking(self):
        """Test canceling a booking"""
        booking = Booking.objects.create(**self.valid_booking_data)
        response = self.client.post(reverse('cancel_booking', args=[booking.id]))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(Booking.objects.count(), 0)

    def test_edit_booking_view_get(self):
        """Test GET request to edit booking"""
        booking = Booking.objects.create(**self.valid_booking_data)
        response = self.client.get(reverse('edit_booking', args=[booking.id]))
        self.assertEqual(response.status_code, 200)

    def test_edit_booking_view_post(self):
        """Test POST request to update booking"""
        booking = Booking.objects.create(**self.valid_booking_data)
        updated_data = self.valid_booking_data.copy()
        updated_data['name'] = 'Updated Name'
        response = self.client.post(
            reverse('edit_booking', args=[booking.id]),
            data=updated_data,
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        booking.refresh_from_db()
        self.assertEqual(booking.name, 'Updated Name')

    def test_get_availability(self):
        """Test availability API endpoint"""
        response = self.client.get(reverse('get_availability'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIsInstance(data, dict)
        # Check that some dates are returned
        self.assertGreater(len(data), 0)
