import requests
import os

def sending_email(to, subject, body):
    data = {
        'from':'bilmak.sabrina@gmail.com',
        'to':to,
        'subject': subject,
        'text':body
    }
    
    response =requests.post(
        os.getenv('MAILGUN_API_ENDPOINT'),
        auth= ('api',os.getenv('MAILGUN_API_KEY')),
        data=data
    )
    if response.status_code == 200:
        print('Email was sand')
    else:
        print('Error while sending email')
        
to = 'podeye8889@jeanssi.com'
subject = 'Test email'
body = 'Hello'
sending_email(to, subject, body)