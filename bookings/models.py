from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime, time


class Booking(models.Model):
    """Model for Bachata class bookings"""
    
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    
    AVAILABLE_DAYS = [0, 2, 4]  # Monday, Wednesday, Friday (0=Monday)
    
    # Class times for each level
    CLASS_TIMES = {
        'beginner': {'start': '18:30', 'end': '19:30'},
        'intermediate': {'start': '19:30', 'end': '20:30'},
        'advanced': {'start': '20:30', 'end': '21:30'},
    }
    
    MAX_STUDENTS = 15
    
    name = models.CharField(
        max_length=100,
        help_text="Full name of the student"
    )
    
    phone = models.CharField(
        max_length=50,
        help_text="Contact phone number"
    )
    
    date = models.DateField(
        help_text="Date of the class (must be Monday, Wednesday, or Friday in 2026)"
    )
    
    level = models.CharField(
        max_length=15,
        choices=LEVEL_CHOICES,
        help_text="Class difficulty level"
    )
    
    class_time = models.TimeField(
        help_text="Time of the class"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['date', 'class_time']
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        # Prevent duplicate bookings (same phone, date, and level)
        unique_together = ['phone', 'date', 'level']
    
    def __str__(self):
        return f"{self.name} - {self.get_level_display()} - {self.date}"
    
    def clean(self):
        """Validate booking data"""
        super().clean()

        # Skip deep validation until required fields are present
        if not self.date:
            return
        
        # Validate year is 2026
        if self.date.year != 2026:
            raise ValidationError({'date': 'Bookings are only available for 2026.'})
        
        # Validate day of week (Monday, Wednesday, Friday only)
        if self.date.weekday() not in self.AVAILABLE_DAYS:
            raise ValidationError({
                'date': 'Classes are only available on Mondays, Wednesdays, and Fridays.'
            })
        
        # Validate class time matches the level (only if class_time is set)
        if self.class_time:
            expected_time = self.CLASS_TIMES[self.level]['start']
            if self.class_time.strftime('%H:%M') != expected_time:
                raise ValidationError({
                    'class_time': f'{self.get_level_display()} classes must be at {expected_time}.'
                })
        
        # Check if class is full
        existing_bookings = Booking.objects.filter(
            date=self.date,
            level=self.level
        ).exclude(pk=self.pk).count()
        
        if existing_bookings >= self.MAX_STUDENTS:
            raise ValidationError({
                'level': f'The {self.get_level_display()} class on {self.date} is fully booked.'
            })
    
    def save(self, *args, **kwargs):
        """Override save to set class_time based on level"""
        if not self.class_time:
            time_str = self.CLASS_TIMES[self.level]['start']
            hour, minute = map(int, time_str.split(':'))
            self.class_time = time(hour, minute)
        
        self.full_clean()
        super().save(*args, **kwargs)
    
    @classmethod
    def get_availability(cls, date, level):
        """Check if a class is available for booking"""
        count = cls.objects.filter(date=date, level=level).count()
        return {
            'available': count < cls.MAX_STUDENTS,
            'spots_left': cls.MAX_STUDENTS - count,
            'total': cls.MAX_STUDENTS
        }
    
    @classmethod
    def get_all_availability_for_date(cls, date):
        """Get availability for all levels on a specific date"""
        return {
            level: cls.get_availability(date, level)
            for level, _ in cls.LEVEL_CHOICES
        }
