// Calendar configuration
const AVAILABLE_DAYS = [1, 3, 5]; // Monday, Wednesday, Friday
let currentMonth = 0; // January 2026
let currentYear = 2026;
let selectedDate = null;

const months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
];

function generateCalendar(month, year) {
    const calendarDays = document.getElementById('calendarDays');
    calendarDays.innerHTML = '';
    
    const firstDay = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const daysInPrevMonth = new Date(year, month, 0).getDate();
    
    // Previous month days
    for (let i = firstDay - 1; i >= 0; i--) {
        const day = daysInPrevMonth - i;
        const dayElement = createDayElement(day, true, false);
        calendarDays.appendChild(dayElement);
    }
    
    // Current month days
    for (let day = 1; day <= daysInMonth; day++) {
        const date = new Date(year, month, day);
        const dayOfWeek = date.getDay();
        const isAvailable = AVAILABLE_DAYS.includes(dayOfWeek);
        const dayElement = createDayElement(day, false, isAvailable, date);
        calendarDays.appendChild(dayElement);
    }
    
    // Next month days
    const totalCells = calendarDays.children.length;
    const remainingCells = 35 - totalCells; // Show 5 weeks
    for (let day = 1; day <= remainingCells; day++) {
        const dayElement = createDayElement(day, true, false);
        calendarDays.appendChild(dayElement);
    }
    
    document.getElementById('currentMonth').textContent = `${months[month]} ${year}`;
}

function createDayElement(day, isOtherMonth, isAvailable, date = null) {
    const dayElement = document.createElement('div');
    dayElement.className = 'calendar-day';
    dayElement.textContent = day;
    
    if (isOtherMonth) {
        dayElement.classList.add('other-month');
    } else if (!isAvailable) {
        dayElement.classList.add('disabled');
    } else {
        dayElement.classList.add('available');
        dayElement.onclick = () => selectDate(date, dayElement);
    }
    
    return dayElement;
}

function selectDate(date, element) {
    // Remove previous selection
    document.querySelectorAll('.calendar-day.selected').forEach(el => {
        el.classList.remove('selected');
    });
    
    // Add selection to clicked day
    element.classList.add('selected');
    selectedDate = date;
    
    // Update form date field
    const dateStr = date.toISOString().split('T')[0];
    const dateInput = document.getElementById('id_date');
    if (dateInput) {
        dateInput.value = dateStr;
    }
    
    // Load availability for this date
    loadAvailability(dateStr);
}

async function loadAvailability(dateStr) {
    try {
        const response = await fetch(`/api/bookings/${dateStr}/`);
        const data = await response.json();
        
        // Update level options with availability
        const levelSelect = document.getElementById('id_level');
        if (levelSelect) {
            Array.from(levelSelect.options).forEach(option => {
                if (option.value) {
                    const level = option.value;
                    const isAvailable = data.availability[level];
                    const count = data.counts[level];
                    
                    if (!isAvailable) {
                        option.disabled = true;
                        const originalText = option.textContent.replace(' (FULL)', '');
                        option.textContent = originalText + ' (FULL)';
                    } else {
                        option.disabled = false;
                        // Reset text if it was marked as full before
                        option.textContent = option.textContent.replace(' (FULL)', '');
                    }
                }
            });
        }
    } catch (error) {
        console.error('Error loading availability:', error);
    }
}

// Navigation
document.getElementById('prevMonth').onclick = () => {
    if (currentMonth === 0 && currentYear === 2026) {
        return; // Don't go before January 2026
    }
    
    currentMonth--;
    if (currentMonth < 0) {
        currentMonth = 11;
        currentYear--;
    }
    generateCalendar(currentMonth, currentYear);
};

document.getElementById('nextMonth').onclick = () => {
    if (currentMonth === 11 && currentYear === 2026) {
        return; // Don't go past December 2026
    }
    
    currentMonth++;
    if (currentMonth > 11) {
        currentMonth = 0;
        currentYear++;
    }
    generateCalendar(currentMonth, currentYear);
};

// Level selector info
const levelSelect = document.getElementById('id_level');
if (levelSelect) {
    levelSelect.onchange = function() {
        document.querySelectorAll('.level-info').forEach(el => el.classList.remove('show'));
        
        const selectedLevel = this.value;
        if (selectedLevel) {
            const infoId = 'levelInfo' + selectedLevel.charAt(0).toUpperCase() + selectedLevel.slice(1);
            const infoElement = document.getElementById(infoId);
            if (infoElement) {
                infoElement.classList.add('show');
            }
        }
    };
}

// Initialize calendar
generateCalendar(currentMonth, currentYear);
