import smtplib
from config import from_email, password, to_email


def sendEmail(bodyMessage):
    # add a subject line and scan results in the body of email
    msg = f'Subject: Count Lines of Code Results\n\n{bodyMessage}'
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        try:
            # encrypt the traffic
            smtp.starttls()

            # say hello to the server over the encrypted channel
            smtp.ehlo()

            # login in with gmail account
            smtp.login(from_email, password)

            # to send email with message
            smtp.sendmail(from_email, to_email, msg)
            print('Email with scan results sent.\n')
        except:
            print('Failed to send email.\n')
