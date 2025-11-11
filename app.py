import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

from flask import Flask,request,render_template,redirect,url_for
import numpy as np
import pandas as pd


from sklearn.preprocessing import StandardScaler

application=Flask(__name__, static_folder='static')

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            # Get form data
            name = request.form.get('name')
            email = request.form.get('email')
            subject = request.form.get('subject')
            message = request.form.get('message')
            
            # Create email content
            email_subject = f"Contact Form: {subject}"
            email_body = f"""
New Contact Form Submission from Bankruptcy Predictor

From: {name}
Email: {email}
Subject: {subject}

Message:
{message}

---
Sent from Bankruptcy Predictor Web App
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            """
            
            # Create MIME message
            msg = MIMEMultipart()
            msg['From'] = 'bankruptcypredictor@noreply.com'
            msg['To'] = 'ayoubdaoudi2001@gmail.com'
            msg['Subject'] = email_subject
            msg['Reply-To'] = email
            
            msg.attach(MIMEText(email_body, 'plain'))
            
            try:
                # Try to send email using SMTP
                # For Gmail, you need to:
                # 1. Enable 2-factor authentication
                # 2. Generate an App Password
                # 3. Use the App Password instead of your regular password
                
                # Uncomment and configure these lines when you have SMTP credentials
                # smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
                # smtp_server.starttls()
                # smtp_server.login('your-email@gmail.com', 'your-app-password')
                # smtp_server.send_message(msg)
                # smtp_server.quit()
                
                # For now, log the message (email will not actually be sent)
                logging.info(f"Contact form submission from {name} ({email})")
                logging.info(f"Subject: {subject}")
                logging.info(f"Message: {message}")
                logging.info("Note: Email not sent. Configure SMTP settings in app.py to enable email sending.")
                
                return render_template('contact.html', success=True)
            except Exception as smtp_error:
                logging.error(f"SMTP Error: {smtp_error}")
                return render_template('contact.html', error="Failed to send email. Please try again later.")
                
        except Exception as e:
            logging.error(f"Contact form error: {e}")
            return render_template('contact.html', error="An error occurred. Please try again.")
    
    return render_template('contact.html')

@app.route('/predictdata',methods=['GET','POST'])
def predictdata():
    from src.pipline.predict_pipline import CustomData, PredictPipeline
    if request.method=='GET':
        return render_template('predictdata.html')
    else:
        data=CustomData(
            atr1=float(request.form.get('atr1')),
            atr2=float(request.form.get('atr2')),
            atr3=float(request.form.get('atr3')),
            atr4=float(request.form.get('atr4')),
            atr5=float(request.form.get('atr5')),
            atr6=float(request.form.get('atr6')),
            atr7=float(request.form.get('atr7')),
            atr8=float(request.form.get('atr8')),
            atr9=float(request.form.get('atr9')),
            atr10=float(request.form.get('atr10')),
            atr11=float(request.form.get('atr11')),
            atr12=float(request.form.get('atr12')),
            atr13=float(request.form.get('atr13')),
            atr14=float(request.form.get('atr14')),
            atr15=float(request.form.get('atr15')),
            atr16=float(request.form.get('atr16')),
            atr17=float(request.form.get('atr17')),
            atr18=float(request.form.get('atr18')),
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)

        predict_pipline=PredictPipeline()
        results = predict_pipline.predict(pred_df)
        logging.info(f"the prediction is {results}")
        if results[0]==1:
            return render_template('predictTrue.html')
        else:
            return render_template('predictFalse.html')

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)