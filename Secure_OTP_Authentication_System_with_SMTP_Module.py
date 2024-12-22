import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def mail_verify(mail):
    otp = random.randint(1111, 9999)

    smtp_server = 'smtp.gmail.com'
    smtp_port = '587'

    mail_user_name = 'Your_Mail_Id'
    mail_password = 'Your_Mail_App_Password'

    from_email = 'Your_Mail_Id'
    to_email = mail
    subject = 'OTP For Validation'
    body = f'OTP for Validation is {otp}'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(mail_user_name, mail_password)
    server.send_message(msg)
    server.quit()

    validate = int(input('Enter OTP for Verification: '))
    if validate == otp:
        return True
    else:
        return False




