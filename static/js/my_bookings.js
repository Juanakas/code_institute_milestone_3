async function searchBookings() {
    const phone = document.getElementById('phoneSearch').value.trim();
    
    if (!phone) {
        alert('Please enter your phone number');
        return;
    }
    
    try {
        const response = await fetch(`/api/my-bookings/${encodeURIComponent(phone)}/`);
        const bookings = await response.json();
        
        if (bookings.length === 0) {
            document.getElementById('bookingsContainer').style.display = 'none';
            document.getElementById('noBookings').style.display = 'block';
        } else {
            displayBookings(bookings);
            document.getElementById('bookingsContainer').style.display = 'block';
            document.getElementById('noBookings').style.display = 'none';
        }
    } catch (error) {
        console.error('Error fetching bookings:', error);
        alert('Error loading bookings. Please try again.');
    }
}

function displayBookings(bookings) {
    const container = document.getElementById('bookingsList');
    container.innerHTML = '';
    
    bookings.forEach(booking => {
        const card = document.createElement('div');
        card.className = 'booking-card';
        
        card.innerHTML = `
            <div class="booking-info">
                <div class="booking-date">${booking.date_display}</div>
                <span class="booking-level ${booking.level}">${booking.level.toUpperCase()}</span>
                <div class="booking-time">Time: ${formatTime(booking.class_time)}</div>
                <div style="margin-top: 8px; color: #7f8c8d;">
                    <strong>Name:</strong> ${booking.name}<br>
                    <strong>Phone:</strong> ${booking.phone}
                </div>
            </div>
            <div class="booking-actions">
                <button class="btn-cancel" onclick="cancelBooking(${booking.id})">Cancel Booking</button>
            </div>
        `;
        
        container.appendChild(card);
    });
}

function formatTime(time) {
    const [hours, minutes] = time.split(':');
    const hour = parseInt(hours);
    const ampm = hour >= 12 ? 'PM' : 'AM';
    const displayHour = hour > 12 ? hour - 12 : (hour === 0 ? 12 : hour);
    return `${displayHour}:${minutes} ${ampm}`;
}

async function cancelBooking(bookingId) {
    if (!confirm('Are you sure you want to cancel this booking?')) {
        return;
    }
    
    try {
        // Get CSRF token
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]')?.value || 
                         getCookie('csrftoken');
        
        const response = await fetch(`/api/cancel/${bookingId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json'
            }
        });
        
        const result = await response.json();
        
        if (result.success) {
            alert('Booking cancelled successfully');
            searchBookings(); // Refresh the list
        } else {
            alert('Error cancelling booking: ' + result.message);
        }
    } catch (error) {
        console.error('Error cancelling booking:', error);
        alert('Error cancelling booking. Please try again.');
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Allow search on Enter key
document.getElementById('phoneSearch').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        searchBookings();
    }
});
