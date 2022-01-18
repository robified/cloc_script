import smtplib
from config import from_email, password, to_email
from email.message import EmailMessage


def sendEmail():
    subject = 'Count Lines of Code'
    plain_body = 'The scan results are attached in this email.'

    msg = EmailMessage()
    msg['subject'] = subject
    msg['from'] = from_email
    msg['to'] = to_email

    msg.set_content(plain_body)

    with open('out.txt') as f:
        msg.add_attachment(f.read(), filename="out.txt")

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        try:
            # encrypt the traffic
            smtp.starttls()

            # say hello to the server over the encrypted channel
            smtp.ehlo()

            # login in with gmail account
            smtp.login(from_email, password)

            # to send email with message
            smtp.send_message(msg)

            print('Email with scan results sent.\n')
        except:
            print('Failed to send email.\n')
