import smtplib
from email.message import EmailMessage
import imghdr

SENDER = 'jeevasathappan2000@gmail.com'
PASSWORD = 'ksxjfunpqbjyyrzs'
RECEIVER = 'jeevasathappan2000@gmail.com'

def send_mail(image_path):
    print('Send mail function started')
    email_message = EmailMessage()  # It's a kind of dictionary
    email_message['Subject'] = 'New Customer In!'
    email_message.set_content('Hey, We just saw a new customer')

    with open(image_path, 'rb') as file:
        content = file.read()
    email_message.add_attachment(content, maintype='image',
                                 subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER,email_message.as_string())
    gmail.quit()
    print('Send email function ended')


if __name__ == '__main__':
    send_mail('images/67.png')