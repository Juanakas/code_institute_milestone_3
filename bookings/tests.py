from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import datetime, date, time
from .models import Booking


class BookingModelTest(TestCase):
    """Test cases for Booking model"""
    
    def setUp(self):
        """Set up test data"""
        self.valid_data = {
            'name': 'John Doe',
            'phone': '+1234567890',
            'date': date(2026, 1, 5),  # Monday, January 5, 2026
            'level': 'beginner',
        }
    
    def test_create_valid_booking(self):
        """Test creating a valid booking"""
        booking = Booking.objects.create(**self.valid_data)
        self.assertEqual(booking.name, 'John Doe')
        self.assertEqual(booking.level, 'beginner')
        self.assertEqual(booking.class_time, time(18, 30))
    
    def test_booking_on_invalid_day(self):
        """Test that booking on non-class days raises validation error"""
        data = self.valid_data.copy()
        data['date'] = date(2026, 1, 6)  # Tuesday
        booking = Booking(**data)
        with self.assertRaises(ValidationError):
            booking.full_clean()
    
    def test_booking_wrong_year(self):
        """Test that bookings for non-2026 years raise validation error"""
        data = self.valid_data.copy()
        data['date'] = date(2025, 1, 5)
        booking = Booking(**data)
        with self.assertRaises(ValidationError):
            booking.full_clean()
    
    def test_duplicate_booking_prevention(self):
        """Test that duplicate bookings are prevented"""
        Booking.objects.create(**self.valid_data)
        duplicate = Booking(**self.valid_data)
        with self.assertRaises(ValidationError):
            duplicate.full_clean()

    def test_booking_str_method(self):
        """Test the string representation of a booking"""
        booking = Booking.objects.create(**self.valid_data)
        expected_str = "John Doe - Beginner - 2026-01-05"
        self.assertEqual(str(booking), expected_str)

    def test_beginner_class_time(self):
        """Test that beginner level gets correct class time"""
        data = self.valid_data.copy()
        data['level'] = 'beginner'
        booking = Booking.objects.create(**data)
        self.assertEqual(booking.class_time, time(18, 30))

    def test_intermediate_class_time(self):
        """Test that intermediate level gets correct class time"""
        data = self.valid_data.copy()
        data['level'] = 'intermediate'
        booking = Booking.objects.create(**data)
        self.assertEqual(booking.class_time, time(19, 30))

    def test_advanced_class_time(self):
        """Test that advanced level gets correct class time"""
        data = self.valid_data.copy()
        data['level'] = 'advanced'
        booking = Booking.objects.create(**data)
        self.assertEqual(booking.class_time, time(20, 30))
