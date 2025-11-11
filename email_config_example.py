"""
Email Configuration Example for Contact Form

To enable actual email sending, follow these steps:

1. For Gmail:
   - Go to your Google Account settings
   - Enable 2-Step Verification
   - Generate an App Password: https://myaccount.google.com/apppasswords
   - Use the App Password instead of your regular password

2. Create a file named 'email_config.py' (not tracked in git) with:

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'your-email@gmail.com'
SENDER_PASSWORD = 'your-app-password'  # Use App Password, not regular password
RECEIVER_EMAIL = 'ayoubdaoudi2001@gmail.com'

3. Update app.py to import and use these settings:

from email_config import SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL

# In the contact route, replace the logging section with:
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(SENDER_EMAIL, SENDER_PASSWORD)
text = msg.as_string()
server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, text)
server.quit()

4. Add 'email_config.py' to .gitignore to keep credentials secure

Alternative: Use environment variables for better security
"""

# Example configuration (DO NOT use in production with real credentials)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'your-email@gmail.com'
SENDER_PASSWORD = 'your-app-password-here'
RECEIVER_EMAIL = 'ayoubdaoudi2001@gmail.com'
