from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_email(name, email):
    context = {
        'name': name,
        'email': email,
    }

    email_subject = 'Thank you for registering'
    email_body = render_to_string('email_message.txt', context)

    email = EmailMessage(
        email_subject, email_body,
        settings.EMAIL_HOST_USER, [email, ],
    )
    return email.send(fail_silently=False)
