from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """Form for creating a booking"""
    
    class Meta:
        model = Booking
        fields = ['name', 'phone', 'date', 'level']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., +1234567890',
                'required': True
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True
            }),
            'level': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
        }
        labels = {
            'name': 'Full Name',
            'phone': 'Phone Number',
            'date': 'Selected Date',
            'level': 'Class Level',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize level choices display
        self.fields['level'].choices = [('', '-- Select a level --')] + [
            (level, f'{label} ({Booking.CLASS_TIMES[level]["start"]} - {Booking.CLASS_TIMES[level]["end"]})')
            for level, label in Booking.LEVEL_CHOICES
        ]
