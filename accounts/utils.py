from django.conf import settings
from twilio.rest import Client

def send_sms(to, code):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f'Your verification code is: {code}',
        from_=settings.TWILIO_PHONE_NUMBER,
        to=to
    )
    return message.sid
