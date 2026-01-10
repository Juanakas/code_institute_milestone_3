"""
Google Sheets integration for bachata bookings
"""
import gspread
from google.oauth2.service_account import Credentials
from django.conf import settings
import logging
import os

logger = logging.getLogger(__name__)


class GoogleSheetsHandler:
    """Handle Google Sheets operations for bookings"""
    
    SCOPES = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    
    def __init__(self):
        """Initialize Google Sheets client"""
        self.client = None
        self.credentials_file = settings.GOOGLE_CREDENTIALS_FILE
        
        # Check if credentials file exists
        if not os.path.exists(self.credentials_file):
            logger.warning(f"Google Sheets credentials file not found at {self.credentials_file}. Google Sheets integration disabled.")
            return
        
        try:
            creds = Credentials.from_service_account_file(
                self.credentials_file,
                scopes=self.SCOPES
            )
            self.client = gspread.authorize(creds)
            logger.info("Google Sheets client initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Google Sheets: {e}")
            self.client = None
    
    def get_worksheet(self):
        """Get or create the bookings worksheet"""
        if not self.client:
            return None
            
        try:
            # Open the spreadsheet by ID
            spreadsheet = self.client.open_by_key(settings.GOOGLE_SHEET_ID)
            
            # Get the first worksheet or create one
            try:
                worksheet = spreadsheet.sheet1
            except:
                worksheet = spreadsheet.add_worksheet(
                    title="Bookings",
                    rows=1000,
                    cols=10
                )
            
            # Initialize headers if the sheet is empty
            if not worksheet.get_all_values():
                worksheet.append_row([
                    'Booking ID',
                    'Name',
                    'Phone',
                    'Date',
                    'Level',
                    'Class Time',
                    'Booked At',
                    'Status'
                ])
            
            return worksheet
        except Exception as e:
            logger.error(f"Failed to get worksheet: {e}")
            return None
    
    def add_booking(self, booking):
        """Add a booking to the Google Sheet"""
        worksheet = self.get_worksheet()
        if not worksheet:
            logger.warning("Google Sheets not configured - skipping export")
            return False
        
        try:
            row_data = [
                str(booking.id),
                booking.name,
                booking.phone,
                booking.date.strftime('%Y-%m-%d'),
                booking.get_level_display(),
                booking.class_time.strftime('%H:%M'),
                booking.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'Active'
            ]
            worksheet.append_row(row_data)
            logger.info(f"Successfully added booking {booking.id} to Google Sheets")
            return True
        except Exception as e:
            logger.error(f"Failed to add booking to Google Sheets: {e}")
            return False
    
    def update_booking(self, booking):
        """Update a booking in the Google Sheet"""
        worksheet = self.get_worksheet()
        if not worksheet:
            return False
        
        try:
            # Find the row with the booking ID
            cell = worksheet.find(str(booking.id))
            if cell:
                row_num = cell.row
                worksheet.update(f'A{row_num}:H{row_num}', [[
                    str(booking.id),
                    booking.name,
                    booking.phone,
                    booking.date.strftime('%Y-%m-%d'),
                    booking.get_level_display(),
                    booking.class_time.strftime('%H:%M'),
                    booking.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    'Active'
                ]])
                logger.info(f"Successfully updated booking {booking.id} in Google Sheets")
                return True
        except Exception as e:
            logger.error(f"Failed to update booking in Google Sheets: {e}")
            return False
    
    def delete_booking(self, booking_id):
        """Mark a booking as deleted in the Google Sheet"""
        worksheet = self.get_worksheet()
        if not worksheet:
            return False
        
        try:
            cell = worksheet.find(str(booking_id))
            if cell:
                row_num = cell.row
                worksheet.update(f'H{row_num}', [['Cancelled']])
                logger.info(f"Successfully marked booking {booking_id} as cancelled in Google Sheets")
                return True
        except Exception as e:
            logger.error(f"Failed to mark booking as cancelled in Google Sheets: {e}")
            return False


# Singleton instance
sheets_handler = GoogleSheetsHandler()
