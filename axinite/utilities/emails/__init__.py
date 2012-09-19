from django.core.mail import EmailMessage

#----------------------------------------------------------------------------
def send_registration_email(message, subject, address):
    email = EmailMessage(subject, message, to=[address])
    email.send()
#----------------------------------------------------------------------------
    
