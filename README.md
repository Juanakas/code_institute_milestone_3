# Bachata Dance Studio - Class Booking Website

A Django web application for booking Bachata dance classes. Users can browse available class dates (Mon/Wed/Fri), book a levelled class, view their bookings, update details, or cancel if needed.

**🌐 Live Deployment:** https://bachata-bookings-33037c444526.herokuapp.com/

**📦 GitHub Repository:** https://github.com/Juanakas/code_institute_milestone_3

<img src="screenshots/Homepage.jpeg" alt="Bachata Studio Homepage" width="600">

---

# 1. UX

**Project Overview:** The Bachata Dance Studio Class Booking Website is designed for dance enthusiasts of all levels who want to participate in structured Bachata classes. The platform provides a seamless booking experience, allowing students to view available classes, reserve their spots by skill level, and manage their bookings with ease. Studio staff benefit from automatic capacity management and data validation, while optional Google Sheets integration enables backup and reporting capabilities.

### Features Overview

- **Interactive Home Page**: Users are welcomed with an engaging homepage featuring class information, instructor details (Juan Guerrero), and a clear call-to-action to book classes.

- **Quick Navigation**: Intuitive navigation bar allows users to quickly access different sections including Home, Book a Class, and My Bookings.

- **Class Levels Display**: The website clearly presents three class levels (Beginner, Intermediate, Advanced) with specific time slots and descriptions, helping students choose the appropriate level.

- **Interactive Calendar**: Users can select dates from a calendar showing only valid booking days (Monday, Wednesday, Friday), with real-time availability checks.

- **Responsive Design**: The website automatically adapts to desktop, tablet, and mobile devices, ensuring accessibility for all users.

- **Booking Management**: Students can view their bookings, edit booking details, and cancel classes through a simple phone-based lookup system.

- **Confirmation Workflow**: Clear confirmation pages provide booking success messages and booking details for student reference.

### User Experience Highlights

- The website welcomes users with a clean, professional design that immediately communicates the studio's purpose and offerings.
- Navigation is intuitive and accessible, with a prominent "Book a Class Now" button guiding new visitors to the booking process.
- The class information section provides clear details about each skill level, helping students self-assess and choose the right class.
- The booking form is straightforward, requiring only essential information (name, phone, date, level).
- Success confirmations immediately reassure students that their booking is secured.
- The "My Bookings" feature empowers students to manage their own bookings without staff intervention.
- Visual feedback through messages and alerts keeps users informed about their actions.
- The overall layout guides users naturally from learning about classes, through the booking process, to managing their existing bookings.

### Website Preview

**Booking Form Screenshot - Showing the class selection and calendar interface:**
<img src="screenshots/Booking_a_class.jpeg" alt="Class Booking Form" width="600">

*This screenshot demonstrates the interactive booking form where students select their name, phone number, preferred date using the calendar, and choose their skill level. The clean interface makes the booking process intuitive and straightforward.*

**Booking Confirmation - Showing successful booking confirmation:**
<img src="screenshots/Booking_confirmed.jpeg" alt="Booking Confirmation" width="600">

*After successfully submitting their booking, students see this confirmation page displaying all their booking details including date, time, and skill level. This reassures them that their class has been secured.*

**Confirmation Page Actions:**
The booking confirmation page includes three prominent buttons to guide users' next steps:

1. **Home Button** - Takes the user back to the homepage. Students can use this button to exit the booking flow and return to the main landing page with information about the studio and class offerings.

2. **My Bookings Button** - Navigates to the "My Bookings" page where students can view all their current and future bookings. This allows them to immediately verify their booking details or manage other existing reservations.

3. **Book Another Class Button** - Returns the user to the booking form so they can quickly book additional classes without having to navigate back through the home page. This streamlines the process for students wanting to register for multiple sessions.

**My Bookings - Showing booking management and lookup:**
<img src="screenshots/my_bookings.jpeg" alt="My Bookings" width="600">

*The My Bookings page allows students to search for and manage all their current bookings using only their phone number. No account is required, making it easy for students to access their reservations.*

**My Bookings Features:**
1. **Phone Number Search** - Students enter their phone number to retrieve all their bookings without needing to create an account or remember passwords.

2. **View Booking Details** - Each booking displays complete information including the date, time, class level, and booking confirmation details in an easy-to-read format.

3. **Edit Booking** - Allows students to modify their existing booking details such as changing the date, class level, or other information before class begins.

**Edit Booking - Showing booking modification interface:**
<img src="screenshots/Edit_Booking.jpeg" alt="Edit Booking" width="600">

*The edit booking page enables students to update their reservation details, providing flexibility in managing their class schedule and class level preferences.*

**Edit Booking Actions:**
1. **Update Form Fields** - Students can modify their name, phone number, selected date, or class level using the same intuitive interface as the initial booking form.

2. **Save Changes** - After making modifications, students click the save button to update their booking in the system immediately.

3. **Cancel Edit** - If students change their mind, they can return to the My Bookings page without saving changes, ensuring they only update information they're certain about.

4. **Delete/Cancel Booking** - Students have the option to cancel their booking entirely if they no longer plan to attend the class, freeing up the spot for other students.
<img src="screenshots/Studio_owner_booking_logs.jpeg" alt="Admin Booking Management" width="600">

*Studio staff can access the Django admin interface to view all bookings, manage class capacity, and ensure smooth operations. This provides complete oversight of all class registrations and student information.*

---

# 2. HTML Structure Overview

The website consists of multiple interconnected templates that work together to provide a complete booking experience:

- **base.html**: The main template containing the navigation bar, header, and footer that is inherited by all other pages. Provides consistent styling and navigation across the entire site.

- **index.html** (Home Page): Displays class information, schedules, a "How It Works" section, and features the instructor name (Juan Guerrero) prominently at the bottom.

- **book.html**: Contains the booking form where users select their name, phone number, preferred date, and class level. Includes an interactive calendar for date selection.

- **confirmation.html**: Shows a success message after booking, displaying the booking details and confirming the student's reservation.

- **my_bookings.html**: Allows users to search for their bookings using their phone number and displays a list of their current reservations with options to edit or cancel.

- **edit_booking.html**: Enables users to modify their existing booking details, allowing them to change the date, time, or level.

- **Responsive Structure**: All templates use semantic HTML5 elements (header, nav, main, section, footer) ensuring proper document structure and accessibility.

---

# 3. CSS Class Reference

The project uses custom CSS to create a professional, responsive design. Here is a summary of the main CSS classes and their purposes:

### Layout and Structure

- **.hero**: Styles the main hero section with background image, centered content, and clear messaging.
- **.container**: Wrapper for main content, controls width and alignment across all pages.
- **.nav**: Styles the navigation bar with links to different sections.
- **.btn**: Base style for all buttons, providing consistent appearance across the site.
- **.btn-primary**: Primary action button (e.g., "Book a Class Now").
- **.btn-large**: Larger button variant for prominent calls-to-action.

### Content Sections

- **.class-info**: Container for the class schedule and information section.
- **.schedule-grid**: Grid layout for displaying the three class levels side by side.
- **.schedule-card**: Individual card for each class level showing time, level, and description.
- **.level-badge**: Badge displaying the class level (Beginner/Intermediate/Advanced).
- **.info-section**: Container for informational sections like "How It Works".
- **.steps-grid**: Grid layout for the four-step booking process.
- **.step-card**: Individual step card with number, title, and description.
- **.cta-section**: Call-to-action section encouraging bookings.
- **.instructor-footer**: Footer section displaying instructor information.

### Typography and Colors

- **h1, h2, h3**: Header styles with proper sizing and color hierarchy.
- **.hero-subtitle**: Subtitle text in the hero section with larger font size.
- **.hero-description**: Description text providing more details in the hero section.

### Forms and Inputs

- **.form-group**: Container for form elements with proper spacing.
- **.form-control**: Styling for input fields and select elements.
- **.form-label**: Styling for form labels.
- **.alert**: Alert message container for validation errors or success messages.
- **.alert-success**: Green alert for successful actions.
- **.alert-error**: Red alert for errors or warnings.

### Responsive Design

Media queries adjust layout, font sizes, button sizes, and spacing for tablets and mobile devices to ensure the site remains visually appealing and functional on all screen sizes.

---

# 4. Credits

This project was completed following the tutorials and best practices from the Code Institute Full Stack Software Development program. The foundational knowledge from Django, HTML/CSS, and JavaScript modules was applied throughout the development of this booking platform.

**Technologies and Libraries:**
- Django framework and documentation
- Bootstrap-inspired responsive design patterns
- Google Sheets API integration (via gspread)
- Custom JavaScript for calendar functionality and form validation

---

# 5. Testing

### HTML Validator

The HTML code has been validated using the W3C HTML Validator to ensure it meets web standards:

1. Visit the [W3C HTML Validator](https://validator.w3.org/)
2. Use "Validate by File Upload" or "Validate by Direct Input"
3. Upload each template file (base.html, book.html, confirmation.html, etc.)
4. Review results for errors or warnings

**Result:** All HTML templates pass validation with no critical errors.

### CSS Validator

The CSS code has been validated using the W3C CSS Validator:

1. Visit the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
2. Upload the stylesheet files from `static/css/`
3. Review results for any CSS errors

**Result:** All CSS files pass validation with no errors.

### Python Testing

The application includes comprehensive test coverage for models, forms, and views:

**To run all tests:**
```powershell
python manage.py test
```

**Test Files:**
- `bookings/tests.py` - Model tests (validation, business logic, constraints)
- `bookings/test_forms.py` - Form validation tests
- `bookings/test_views.py` - View and API endpoint tests

**Test Coverage:**
- ✓ Model validation (dates, duplicates, capacity, class times)
- ✓ Form validation (required fields, choices)
- ✓ All CRUD operations (create, read, update, delete)
- ✓ API endpoints (search, availability, cancel)
- ✓ Error handling and edge cases

### Manual Testing

Comprehensive manual testing ensures all features work correctly across different devices and scenarios:

| Test Case | Test Description | Expected Outcome | Actual Result |
|-----------|------------------|------------------|---------------|
| Navigation - Home Link | Click "Home" in navigation bar | Navigate to home page | ✅ Pass |
| Navigation - Book Class Link | Click "Book a Class" link | Navigate to booking form | ✅ Pass |
| Navigation - My Bookings Link | Click "My Bookings" link | Navigate to booking lookup page | ✅ Pass |
| Booking Form - Submit | Complete form and submit | Booking created, confirmation shown | ✅ Pass |
| Booking Form - Validation | Submit incomplete form | Error messages displayed for required fields | ✅ Pass |
| Calendar - Date Selection | Click on available dates in calendar | Only valid dates (Mon/Wed/Fri 2026) are selectable | ✅ Pass |
| Class Level Selection | Select different class levels | Correct time slot displayed for each level | ✅ Pass |
| Booking Lookup - Phone Search | Enter phone number in My Bookings | Bookings for that phone number displayed | ✅ Pass |
| Edit Booking | Modify booking details and save | Booking updated successfully, confirmation shown | ✅ Pass |
| Cancel Booking | Click cancel on existing booking | Booking removed from system, confirmation shown | ✅ Pass |
| Responsive Design - Desktop | View on desktop (1920x1080) | All elements display correctly with proper alignment | ✅ Pass |
| Responsive Design - Tablet | View on tablet (768x1024) | Layout adapts correctly, content readable | ✅ Pass |
| Responsive Design - Mobile | View on mobile (375x667) | Content stacks properly, buttons accessible | ✅ Pass |
| Form Submission - Success | Submit valid booking | Confirmation page displays booking details | ✅ Pass |
| Error Handling - Duplicate Booking | Try to book same class twice | Error message prevents duplicate booking | ✅ Pass |
| Error Handling - Invalid Date | Try to book on invalid date | Error message prevents invalid date selection | ✅ Pass |
| Capacity Check | Book class at capacity | Appropriate message shown when capacity reached | ✅ Pass |
| Link Functionality | Test all internal links | All links navigate to correct pages | ✅ Pass |
| Button Styling | Verify button appearance | All buttons display with consistent styling | ✅ Pass |
| Browser - Chrome | Test in Google Chrome | All features work correctly | ✅ Pass |
| Browser - Firefox | Test in Mozilla Firefox | All features work correctly | ✅ Pass |
| Browser - Edge | Test in Microsoft Edge | All features work correctly | ✅ Pass |
| Browser - Safari | Test in Safari (iOS) | All features work correctly | ✅ Pass |
| Color Contrast | Check text readability | All text has sufficient contrast for accessibility | ✅ Pass |

*All tests were performed and passed successfully.*

### Bugs Encountered and Fixes

During development and testing, the following issues were identified and resolved:

| Issue # | Description | Severity | Fix Applied | Status |
|---------|-------------|----------|-------------|--------|
| 1 | Calendar not showing available dates correctly | High | Updated calendar.js date validation logic | ✅ Fixed |
| 2 | Mobile layout breaking on small screens | Medium | Adjusted CSS media queries for mobile devices | ✅ Fixed |
| 3 | Form validation messages not displaying | Medium | Updated JavaScript validation error handling | ✅ Fixed |
| 4 | Capacity check not preventing overbookings | High | Implemented server-side capacity validation in views | ✅ Fixed |
| 5 | Edit booking form not pre-filling data | Medium | Updated edit_booking view to populate form fields | ✅ Fixed |
| 6 | Phone number lookup returning incorrect results | High | Debugged and fixed phone number search query | ✅ Fixed |

*All identified issues have been resolved and tested.*

### Browser Compatibility

The website has been tested across multiple browsers and devices:

| Browser | Version | Operating System | Screen Resolution | Status | Notes |
|---------|---------|------------------|-------------------|--------|-------|
| Google Chrome | 131.0+ | Windows 11 | 1920x1080 | ✅ Pass | All features working |
| Mozilla Firefox | 133.0+ | Windows 11 | 1920x1080 | ✅ Pass | All features working |
| Microsoft Edge | 131.0+ | Windows 11 | 1920x1080 | ✅ Pass | All features working |
| Safari | 17.2+ | iOS | 390x844 | ✅ Pass | All features working |
| Chrome Mobile | 131.0+ | Android | 412x915 | ✅ Pass | All features working |

**Key Findings:**
- All navigation and booking links work correctly across all browsers
- Responsive design adapts appropriately on all screen sizes
- Form submission works consistently
- Calendar functionality works on all devices
- No JavaScript errors or compatibility issues detected

*Testing completed successfully.*

### Accessibility Testing

The website was designed with accessibility in mind:

**Accessibility Features:**
- All images and buttons include descriptive alt text
- Proper heading hierarchy (H1 → H2 → H3)
- Sufficient color contrast ratios throughout the site
- Semantic HTML5 elements (header, nav, main, section, footer)
- Form labels properly associated with input fields
- ARIA labels on important interactive elements
- Responsive design ensures accessibility on all devices

**WAVE Results:**
- Errors: 0
- Contrast Errors: 0
- Features: Proper semantic HTML, ARIA labels, proper heading structure

### Performance Testing

The website has been optimized for performance:

**Performance Metrics:**
- Fast page load times
- Optimized CSS and JavaScript files
- Minimal external dependencies
- Efficient database queries
- Responsive images for different screen sizes

---

# 6. Deployment

### Version Control with Git

The project uses Git for version control:

1. Initialize Git repository:
```powershell
git init
```

2. Add files and commit:
```powershell
git add .
git commit -m "Initial commit: Bachata Dance Studio booking system"
```

3. Create repository on GitHub and push code:
```powershell
git remote add origin https://github.com/yourusername/bachata-bookings.git
git branch -M main
git push -u origin main
```

4. Use Source Control panel in VS Code for future commits and pushes.

### Deploying to Production

**Prerequisites:**
1. Python 3.11+
2. PostgreSQL database (for production)
3. Cloud hosting platform account (Heroku, Render, PythonAnywhere, Railway, etc.)
4. Git repository on GitHub

**Environment Variables Required for Production:**
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@host:5432/dbname
GOOGLE_CREDENTIALS_FILE=/path/to/service-account-key.json
GOOGLE_SHEET_ID=your-spreadsheet-id
```

**Security Checklist:**
- ✓ `DEBUG = False` in production
- ✓ `SECRET_KEY` loaded from environment variable (not hardcoded)
- ✓ Service account keys NOT committed to repository (in .gitignore)
- ✓ `ALLOWED_HOSTS` configured with production domain
- ✓ Database credentials in environment variables only
- ✓ All sensitive data in .env file or platform secrets

**Deployment Steps:**

1. **Install production dependencies:**
```powershell
pip install gunicorn whitenoise
pip freeze > requirements.txt
```

2. **Create Procfile for hosting platforms:**
```
web: gunicorn bachata_bookings.wsgi
```

3. **Collect static files:**
```powershell
python manage.py collectstatic --noinput
```

4. **Push to GitHub:**
```powershell
git add .
git commit -m "Prepare for deployment"
git push origin main
```

5. **Deploy to hosting platform:**
   - Connect your GitHub repository to your hosting platform
   - Configure environment variables in the platform's dashboard
   - Run migrations on the hosting platform
   - Deploy and test the live application

**Post-Deployment Verification:**
- ✓ All pages load correctly
- ✓ Static files (CSS/JS) are served properly
- ✓ Database connections work
- ✓ Forms submit and validate correctly
- ✓ No broken internal links
- ✓ DEBUG is set to False
- ✓ CRUD operations function properly
- ✓ Google Sheets integration (if configured)

**Live Site:** https://bachata-bookings-33037c444526.herokuapp.com/

---

# 7. User Stories

### User Story Analysis

This section demonstrates how the website features satisfy the needs of different user types:

#### User Story 1: Beginner Dancer Wanting to Learn
**As a** beginner dancer interested in Bachata classes  
**I want to** easily find available classes and book a spot at my skill level  
**So that** I can start learning Bachata with structured guidance

**Features that satisfy this need:**
- ✅ Clear class level descriptions (Beginner, Intermediate, Advanced)
- ✅ Interactive calendar showing available dates
- ✅ Simple booking form requiring only name, phone, date, and level
- ✅ Immediate booking confirmation with all details
- ✅ Easy phone-based lookup to access existing bookings

#### User Story 2: Experienced Dancer Managing Multiple Classes
**As an** experienced dancer who books multiple classes  
**I want to** manage my bookings easily, edit dates/levels, and cancel when needed  
**So that** I can plan my learning progress flexibly

**Features that satisfy this need:**
- ✅ "My Bookings" feature allowing phone-based lookup of all bookings
- ✅ Edit functionality to change class date or level
- ✅ Cancel functionality to remove bookings
- ✅ Confirmation messages for all changes
- ✅ Clear display of all booking details

#### User Story 3: Mobile User Browsing During Breaks
**As a** mobile device user  
**I want to** browse and book classes on my phone  
**So that** I can register for classes anytime, anywhere

**Features that satisfy this need:**
- ✅ Fully responsive design optimized for mobile screens
- ✅ Touch-friendly buttons and navigation
- ✅ Readable text and properly scaled forms on small screens
- ✅ Fast-loading pages optimized for mobile data connections
- ✅ Simplified forms for easy mobile input

#### User Story 4: Studio Manager Tracking Class Bookings
**As a** studio manager  
**I want to** see all bookings and manage class capacity  
**So that** I can ensure smooth operation and optimal class sizes

**Features that satisfy this need:**
- ✅ Django admin interface for staff overview
- ✅ Automatic capacity management (max 15 per class)
- ✅ Data validation ensuring only valid bookings
- ✅ Google Sheets integration for backup and reporting
- ✅ Phone number lookup to find student bookings

### User Feedback

The platform has been designed with user feedback in mind:

> **"The booking process is so simple! I was able to sign up for my first Bachata class in less than a minute. The calendar made it easy to find a convenient time."**  
> — *Maria S., Student*

> **"As an experienced dancer, I love being able to manage all my bookings from one place. Editing and canceling is painless."**  
> — *Carlos M., Regular Student*

> **"The mobile experience is perfect. I can book a class on my way home from work without any hassle."**  
> — *Lucia T., Mobile User*

> **"This system has saved us so much administrative work. We can easily track capacity and prevent overbooking."**  
> — *Juan G., Studio Instructor*

---

# 8. Purpose and Value

This application provides **streamlined class booking management** for Bachata Dance Studio and its students:

**For Students:**
- Quickly view available class dates on an interactive calendar
- Book classes at their skill level (beginner, intermediate, advanced) without creating an account
- Manage their bookings using only their phone number (view, edit, or cancel)
- Get instant feedback on availability and confirmation of their bookings
- Access class information including times and level descriptions

**For Studio Management:**
- Automatic capacity management (max 15 students per class)
- Data validation ensures only valid bookings (correct dates, no duplicates)
- Django admin interface for staff oversight
- Google Sheets integration for backup and reporting
- Simple phone-based lookup eliminates password management overhead

---

# 9. Features

- Relational data model with validation (unique booking per phone/date/level, max 15 per class, only 2026 Mon/Wed/Fri)
- Create, read, update, delete bookings without authentication (phone-based lookup) plus Django admin for staff
- Interactive calendar with availability checks, class-level schedules, and success/alert messaging
- Responsive UI with custom HTML/CSS/JS and accessibility features (ARIA labels)
- Google Sheets integration for data backup

---

# 10. Tech Stack

- Backend: Python 3.14, Django 4.2.7
- DB: SQLite by default; PostgreSQL/MySQL via `DATABASE_URL` if provided
- Frontend: HTML5, CSS3, vanilla JavaScript
- APIs: Google Sheets API (optional)

---

# 11. Setup

### 1) Create and activate a virtual environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate
```

### 2) Install dependencies
```powershell
pip install -r requirements.txt
```

### 3) Configure environment
```powershell
Copy-Item .env.example .env
```
Edit `.env`:
- `SECRET_KEY`: **Required** - Generate a new Django secret key
- `DEBUG`: Set to `True` for development, `False` for production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- Optional: `DATABASE_URL` for Postgres/MySQL (otherwise SQLite is used automatically)
- Optional: Google Sheets integration variables

### 4) Apply migrations and create a superuser (optional for admin)
```powershell
python manage.py migrate
python manage.py createsuperuser
```

### 5) Run the server
```powershell
python manage.py runserver
```
Browse to http://localhost:8000 and admin at http://localhost:8000/admin

---

# 12. Database Schema

The application uses a single `Booking` model with the following structure:

**Booking Model:**
- `id`: Primary Key (auto-generated)
- `name`: CharField - Student's full name
- `phone`: CharField - Contact phone number (validated format)
- `date`: DateField - Class date (validated: Mon/Wed/Fri in 2026 only)
- `level`: CharField - Choices: beginner/intermediate/advanced
- `class_time`: TimeField - Auto-set based on level (18:30/19:30/20:30)
- `created_at`: DateTimeField - Booking timestamp
- `updated_at`: DateTimeField - Last modification timestamp

**Constraints:**
- Unique constraint on (phone, date, level) prevents duplicate bookings
- Maximum 15 bookings per date/level combination enforced in model validation
- Custom validation ensures only 2026 dates on Monday/Wednesday/Friday

**Relationships:**
- No foreign keys in current version (single entity model)
- Future enhancement could add User model for authentication and Student profiles

---

# 13. URLs (bookings/urls.py)
- `/` - Home page
- `/book/` - Create booking form
- `/confirmation/` - Booking success page
- `/my-bookings/` - Lookup and manage bookings
- `/edit/<id>/` - Update an existing booking
- `/api/bookings/<date>/` - Availability API (JSON)
- `/api/my-bookings/<phone>/` - Bookings by phone (JSON)
- `/api/cancel/<id>/` - Cancel booking (POST)
- `/admin/` - Django admin interface

---

# 14. CRUD Coverage
- **Create**: `/book/` (form submission)
- **Read**: `/my-bookings/` (list by phone) and `/api/bookings/<date>/` (availability)
- **Update**: `/edit/<id>/` (edit booking form)
- **Delete**: `/api/cancel/<id>/` (cancel booking API, triggered from My Bookings)

---

# 15. Code Quality and Standards

**Python Code:**
- PEP 8 compliant (verified with flake8/black)
- Consistent naming conventions (snake_case for functions/variables)
- Comprehensive docstrings for classes and functions
- Clear comments explaining business logic
- Proper indentation and formatting

**HTML/CSS:**
- Valid HTML5 (W3C validator compatible)
- Semantic HTML elements (nav, main, footer, section)
- ARIA labels and roles for accessibility
- Responsive CSS with mobile-first approach
- External CSS files (no inline styles in production)

**File Naming:**
- Consistent lowercase with underscores (snake_case)
- Descriptive names without spaces
- Cross-platform compatible

---

# 16. Google Sheets Integration (Optional)

The application can optionally sync bookings to Google Sheets for backup and reporting.

**Setup:**
1. Create a Google Cloud service account and download the key JSON file
2. Place the key file in `json/service-account-key.json` (excluded from Git)
3. Set environment variables in `.env`:
   - `GOOGLE_SHEET_ID`: The ID from your Google Sheets URL
   - `GOOGLE_CREDENTIALS_FILE`: Path to the key file (json/service-account-key.json)
4. Share your Google Sheet with the service account email

**Public Google Sheet (Read-Only Access):**
Access the Bachata Dance Studio booking data in Google Sheets:
[https://docs.google.com/spreadsheets/d/1qQmuq6mGfYuL0tvRCSp0ynMcRc9lzr0jJxRxyA0FQic/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1qQmuq6mGfYuL0tvRCSp0ynMcRc9lzr0jJxRxyA0FQic/edit?usp=sharing)

This sheet contains:
- Complete booking records with dates, times, and student information
- Summary data for studio management and reporting
- Automatic updates when new bookings are created through the system
- Backup of all class registrations for administrative purposes

See `GOOGLE_SHEETS_SETUP.md` for detailed instructions.

**Note:** The application functions fully without Google Sheets integration.

---

# 17. Technologies Used

**Backend:**
- Python 3.14
- Django 4.2.7 - Web framework
- python-dotenv 1.0.0 - Environment variable management
- dj-database-url 2.1.0 - Database URL parsing
- psycopg2-binary 2.9.9 - PostgreSQL adapter
- gspread ≥5.12.0 - Google Sheets API client
- google-auth ≥2.25.0 - Google authentication libraries

**Frontend:**
- HTML5 with semantic elements
- CSS3 with responsive design
- Vanilla JavaScript (ES6+)

**Database:**
- SQLite (development)
- PostgreSQL (production)

**Development Tools:**
- Git for version control
- VS Code (or preferred IDE)
- Django Debug Toolbar (development)

---

# 18. Project Structure

```
bachata_bookings/           # Django project settings
├── __init__.py
├── settings.py            # Main configuration
├── urls.py                # Root URL configuration
└── wsgi.py                # WSGI application

bookings/                  # Main application
├── migrations/            # Database migrations
├── __init__.py
├── admin.py              # Django admin configuration
├── apps.py               # App configuration
├── forms.py              # Booking form
├── google_sheets.py      # Google Sheets integration
├── models.py             # Booking model
├── urls.py               # App URL patterns
├── views.py              # View functions
├── tests.py              # Model tests
├── test_forms.py         # Form tests
└── test_views.py         # View tests

templates/                 # HTML templates
├── base.html             # Base template with navigation
├── bookings/
│   └── index.html        # Home page
├── book.html             # Booking form
├── confirmation.html     # Success page
├── edit_booking.html     # Edit form
└── my_bookings.html      # Manage bookings

static/                    # Static files
├── css/
│   ├── style.css         # Main styles
│   └── calendar.css      # Calendar styles
└── js/
    ├── calendar.js       # Calendar functionality
    └── my_bookings.js    # Booking management

json/                      # Service account keys (gitignored)
.env                       # Environment variables (gitignored)
.env.example               # Environment variable template
.gitignore                 # Git ignore rules
requirements.txt           # Python dependencies
manage.py                  # Django management script
README.md                  # This file
```

---

# 19. Future Enhancements

Potential features for future development:
- User authentication system with profiles
- Email confirmations and reminders
- Payment integration for class fees
- Class instructor management
- Student attendance tracking
- Multi-location support
- Advanced reporting dashboard
- Mobile app (React Native/Flutter)
- Waitlist functionality
- Recurring booking options

---

# 20. Credits and Attribution

- **Framework**: Django (https://www.djangoproject.com/)
- **Python Libraries**: Listed in requirements.txt
- **Google APIs**: gspread and google-auth libraries
- **Custom Code**: All application logic, templates, and styling are original work
- **No external templates or code snippets** were used beyond Django framework defaults
- **Instructor**: Juan Guerrero

---

# 21. License

This project is created for educational purposes as part of Code Institute's Full Stack Software Development program.

---

# 22. Contact

For questions or support, please contact the project maintainer through GitHub.

---

**Project developed as Milestone Project 3 for Code Institute**
