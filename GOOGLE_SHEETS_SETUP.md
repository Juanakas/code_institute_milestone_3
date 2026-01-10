# Google Sheets API Setup Instructions

## Step 1: Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click **"Create Project"** or select an existing project
3. Give your project a name (e.g., "Bachata Bookings")
4. Click **"Create"**

## Step 2: Enable Google Sheets API

1. In the Google Cloud Console, go to **"APIs & Services" > "Library"**
2. Search for **"Google Sheets API"**
3. Click on it and press **"Enable"**
4. Also search for **"Google Drive API"** and enable it

## Step 3: Create Service Account Credentials

1. Go to **"APIs & Services" > "Credentials"**
2. Click **"Create Credentials"** > **"Service Account"**
3. Enter a service account name (e.g., "bachata-sheets")
4. Click **"Create and Continue"**
5. Skip the optional steps and click **"Done"**

## Step 4: Create and Download JSON Key

1. Click on the service account you just created
2. Go to the **"Keys"** tab
3. Click **"Add Key" > "Create new key"**
4. Select **"JSON"** format
5. Click **"Create"**
6. The JSON file will automatically download

## Step 5: Setup Credentials in Your Project

1. Rename the downloaded JSON file to `credentials.json`
2. Move it to your project root directory:
   ```
   C:\Users\juanc\OneDrive\Documents\web_developer\code_institute\08_milestone3\credentials.json
   ```

3. **IMPORTANT**: Add to your `.gitignore` file to prevent committing:
   ```
   credentials.json
   ```

## Step 6: Configure Environment Variables (Optional)

Create or update your `.env` file in the project root:

```env
GOOGLE_CREDENTIALS_FILE=credentials.json
GOOGLE_SHEET_NAME=Bachata Bookings
GOOGLE_SHEET_OWNER_EMAIL=your-email@gmail.com
```

Replace `your-email@gmail.com` with your actual Google email.

## Step 7: Share the Spreadsheet (Automatic)

The app will automatically:
- Create a new Google Sheet named "Bachata Bookings"
- Share it with your email (if you set GOOGLE_SHEET_OWNER_EMAIL)

Or you can manually:
1. Open [Google Sheets](https://sheets.google.com)
2. Create a new spreadsheet named "Bachata Bookings"
3. Click **"Share"**
4. Add the service account email (found in credentials.json under "client_email")
5. Give it **"Editor"** permission

## Troubleshooting

### Error: "Credentials file not found"
- Make sure `credentials.json` is in the project root directory
- Check the file path in settings

### Error: "Permission denied"
- Make sure the service account has editor access to your Google Sheet
- Check that Google Sheets API is enabled in Google Cloud Console

### Spreadsheet not found
- The app will create it automatically on first booking
- Or create it manually and share with the service account email

## Testing

1. Restart your Django server
2. Make a test booking
3. Check your Google Sheet - a new row should appear!

## Security Notes

- Never commit `credentials.json` to version control
- Keep your service account key secure
- Only share spreadsheet access with the service account, not publicly
