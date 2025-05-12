import textwrap
from django.core.mail import EmailMessage


def send_email(*, email, subject, text):
    email = EmailMessage(subject, textwrap.dedent(text), to=[email])
    email.send()
