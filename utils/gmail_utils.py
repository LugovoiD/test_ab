import smtplib

gmail_user = ''
gmail_password = ''


def send_email(to, body, sent_from=None, subject=""):
    sent_from = gmail_user if sent_from is None else sent_from
    to = to
    subject = subject
    body = body
    email_text = f'''             
             {body} '''

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
    except Exception as e:
        raise Exception(f'Something went wrong... {e}')
