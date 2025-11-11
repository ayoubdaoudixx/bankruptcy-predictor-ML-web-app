# Email Configuration Guide

This guide will help you set up email functionality for the contact form in your Bankruptcy Predictor application.

## Current Status

The contact form is fully functional and will:
- ✅ Display success/error messages to users
- ✅ Log all contact form submissions to the console
- ⚠️ **NOT send actual emails** (requires configuration)

## How to Enable Email Sending

To enable actual email sending, follow these steps:

### Option 1: Using Gmail (Recommended for Testing)

1. **Enable 2-Factor Authentication on your Gmail account**
   - Go to https://myaccount.google.com/security
   - Enable 2-Step Verification

2. **Generate an App Password**
   - Go to https://myaccount.google.com/apppasswords
   - Select "Mail" and your device
   - Copy the 16-character password

3. **Update app.py**
   
   Open `/Users/mac/Downloads/Bankruptcy/app.py` and find the contact route (around line 67-72).
   
   Uncomment and configure these lines:
   
   ```python
   smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
   smtp_server.starttls()
   smtp_server.login('ayoubdaoudi2001@gmail.com', 'your-16-char-app-password')
   smtp_server.send_message(msg)
   smtp_server.quit()
   ```
   
   Replace `'your-16-char-app-password'` with the App Password you generated.

### Option 2: Using Environment Variables (Recommended for Production)

1. **Create a `.env` file** in the project root:
   
   ```
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USERNAME=ayoubdaoudi2001@gmail.com
   SMTP_PASSWORD=your-app-password
   RECIPIENT_EMAIL=ayoubdaoudi2001@gmail.com
   ```

2. **Install python-dotenv**:
   
   ```bash
   pip install python-dotenv
   ```

3. **Update app.py** to use environment variables:
   
   Add at the top of the file:
   ```python
   from dotenv import load_dotenv
   import os
   
   load_dotenv()
   ```
   
   Then in the contact route:
   ```python
   smtp_server = smtplib.SMTP(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT')))
   smtp_server.starttls()
   smtp_server.login(os.getenv('SMTP_USERNAME'), os.getenv('SMTP_PASSWORD'))
   smtp_server.send_message(msg)
   smtp_server.quit()
   ```

### Option 3: Using Other Email Services

#### SendGrid
- Sign up at https://sendgrid.com
- Get your API key
- Use SendGrid's Python library

#### Mailgun
- Sign up at https://mailgun.com
- Get your API credentials
- Use Mailgun's Python library

## Testing the Contact Form

1. Start your Flask application:
   ```bash
   python app.py
   ```

2. Navigate to: http://localhost:8080/contact

3. Fill out the form and submit

4. Check:
   - Console logs for submission details
   - Your email inbox (if SMTP is configured)

## Security Best Practices

⚠️ **IMPORTANT**: Never commit sensitive credentials to version control!

- Always use environment variables for sensitive data
- Add `.env` to your `.gitignore` file
- Use App Passwords instead of your main Gmail password
- Consider using a dedicated email service for production

## Troubleshooting

### "Authentication failed" error
- Verify your App Password is correct
- Ensure 2-Factor Authentication is enabled
- Check that you're using the correct Gmail account

### "Connection refused" error
- Check your internet connection
- Verify the SMTP server and port are correct
- Some networks block SMTP ports (try port 465 with SSL)

### Emails not being received
- Check spam/junk folder
- Verify the recipient email is correct
- Check Gmail's "Sent" folder to confirm the email was sent

## Contact Form Features

The contact page includes:
- ✨ Modern, responsive design with blue theme
- 📱 Mobile-friendly layout
- ✅ Form validation
- 💬 Success/error messages
- 🎨 Smooth animations and hover effects
- 📧 Contact information display

## Need Help?

If you encounter any issues, check the application logs or contact the developer.
