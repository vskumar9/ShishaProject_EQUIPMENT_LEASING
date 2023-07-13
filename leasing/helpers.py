from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


def send_forget_password_mail(email, token):
    subject = "You forgot your password"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]

    # Render the HTML content of the email using the template
    html_content = render_to_string('forget_password.html', {'token': token})

    # Create the email message object
    email_message = EmailMultiAlternatives(subject, '', email_from, recipient_list)
    email_message.attach_alternative(html_content, "text/html")

    # Send the email
    email_message.send()

    return True
