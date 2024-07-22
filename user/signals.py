from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Goat Farm Management System'
        message = f'Hi {instance.first_name},\n\nWelcome to Goat Farm Management System! Your account has been created successfully.'
        from_email = 'examle@gmail.com'
        recipient_list = [instance.email]
        send_mail(subject, message, from_email, recipient_list)
