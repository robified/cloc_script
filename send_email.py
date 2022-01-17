import smtplib
from config import from_email, password, to_email
from email.message import EmailMessage


def sendEmail(bodyMessage):
    subject = 'Count Lines of Code Results'
    plain_body = f'{bodyMessage}'

    msg = EmailMessage()
    msg['subject'] = subject
    msg['from'] = from_email
    msg['to'] = to_email

    msg.set_content(plain_body)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        try:
            # encrypt the traffic
            smtp.starttls()

            # say hello to the server over the encrypted channel
            smtp.ehlo()

            # login in with gmail account
            smtp.login(from_email, password)

            # to send email with message
            # smtp.sendmail(from_email, to_email, msg)
            smtp.send_message(msg)

            print('Email with scan results sent.\n')
        except:
            print('Failed to send email.\n')
