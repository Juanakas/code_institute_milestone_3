from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from datetime import datetime, time, timedelta
from .models import Booking
from .forms import BookingForm
from .google_sheets import sheets_handler


def index(request):
    """Home page"""
    return render(request, 'bookings/index.html')


def book(request):
    """Booking form page"""
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                booking = form.save(commit=False)
                
                # Set class time based on level
                time_str = Booking.CLASS_TIMES[booking.level]['start']
                hour, minute = map(int, time_str.split(':'))
                booking.class_time = time(hour, minute)
                
                booking.save()
                
                # Send to Google Sheets
                sheets_handler.add_booking(booking)
                
                messages.success(
                    request,
                    f'Successfully booked {booking.get_level_display()} class on {booking.date.strftime("%B %d, %Y")}!'
                )
                return redirect('confirmation')
            except Exception as e:
                messages.error(request, f'Error creating booking: {str(e)}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = BookingForm()
    
    context = {
        'form': form,
    }
    return render(request, 'book.html', context)


def confirmation(request):
    """Booking confirmation page"""
    return render(request, 'confirmation.html')


def my_bookings(request):
    """View user's bookings"""
    return render(request, 'my_bookings.html')


@require_http_methods(["GET"])
def search_booking(request):
    """Search bookings by name and phone for quick lookup."""
    name = request.GET.get('name', '').strip()
    phone = request.GET.get('phone', '').strip()

    if not name or not phone:
        return JsonResponse({'status': 'not_found', 'bookings': []})

    bookings = Booking.objects.filter(name__iexact=name, phone=phone).order_by('date')

    if not bookings.exists():
        return JsonResponse({'status': 'not_found', 'bookings': []})

    data = [
        {
            'id': b.id,
            'name': b.name,
            'phone': b.phone,
            'date': b.date.strftime('%Y-%m-%d'),
            'date_display': b.date.strftime('%B %d, %Y'),
            'level': b.level,
            'class_time': b.class_time.strftime('%H:%M'),
        }
        for b in bookings
    ]

    return JsonResponse({'status': 'found', 'bookings': data})


def edit_booking(request, booking_id):
    """Edit an existing booking (update)"""
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            try:
                booking = form.save(commit=False)
                time_str = Booking.CLASS_TIMES[booking.level]['start']
                hour, minute = map(int, time_str.split(':'))
                booking.class_time = time(hour, minute)
                booking.save()
                
                # Update in Google Sheets
                sheets_handler.update_booking(booking)
                
                messages.success(
                    request,
                    f'Updated {booking.get_level_display()} class on {booking.date.strftime("%B %d, %Y")}.'
                )
                return redirect('my_bookings')
            except Exception as e:
                messages.error(request, f'Error updating booking: {str(e)}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = BookingForm(instance=booking)

    context = {
        'form': form,
        'booking': booking,
    }
    return render(request, 'edit_booking.html', context)


@require_http_methods(["GET"])
def get_availability(request):
    """Return availability for the next 7 days across all levels."""
    today = datetime.now().date()
    availability = {}
    for offset in range(7):
        current_date = today + timedelta(days=offset)
        availability[current_date.strftime('%Y-%m-%d')] = Booking.get_all_availability_for_date(current_date)
    return JsonResponse(availability)


@require_http_methods(["GET"])
def api_bookings_by_date(request, date_str):
    """API endpoint to get bookings for a specific date"""
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        availability = Booking.get_all_availability_for_date(date)
        
        counts = {
            level: Booking.objects.filter(date=date, level=level).count()
            for level, _ in Booking.LEVEL_CHOICES
        }
        
        return JsonResponse({
            'counts': counts,
            'availability': {
                level: info['available']
                for level, info in availability.items()
            }
        })
    except ValueError:
        return JsonResponse({'error': 'Invalid date format'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["GET"])
def api_bookings_by_phone(request, phone):
    """API endpoint to get bookings for a specific phone number"""
    try:
        bookings = Booking.objects.filter(phone=phone).order_by('date')
        bookings_data = []
        
        for booking in bookings:
            bookings_data.append({
                'id': booking.id,
                'name': booking.name,
                'phone': booking.phone,
                'date': booking.date.strftime('%Y-%m-%d'),
                'date_display': booking.date.strftime('%B %d, %Y'),
                'level': booking.level,
                'class_time': booking.class_time.strftime('%H:%M'),
            })
        
        return JsonResponse(bookings_data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["POST"])
def cancel_booking(request, booking_id):
    """Cancel a booking"""
    try:
        booking = get_object_or_404(Booking, id=booking_id)
        
        # Mark as cancelled in Google Sheets before deleting
        sheets_handler.delete_booking(booking_id)

        booking.delete()
        return JsonResponse({
            'status': 'success',
            'success': True,
            'message': 'Booking cancelled successfully'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=500)
