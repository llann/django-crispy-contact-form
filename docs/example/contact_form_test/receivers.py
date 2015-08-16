from contact_form.signals import contact_form_valid
from django.core.mail import send_mail


def sendmail_callback(sender, **kwargs):
    if kwargs['event'] == 'CONTACT_FORM_VALID_MESSAGE':
        send_mail(kwargs['subject'], kwargs['message'], kwargs['sender_email'], 'from@adress.com')

contact_form_valid.connect(sendmail_callback)


def my_callback2(sender, **kwargs):
    if kwargs['event'] == 'CONTACT_FORM_INVALID_MESSAGE':
        print('Form not submitted!')

contact_form_invalid.connect(my_callback2)
