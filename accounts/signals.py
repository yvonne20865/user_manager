from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def send_verification_email(sender, instance, created, **kwargs):
    if created and not instance.is_verified:
        # Here you would generate a verification link/token
        verification_link = f"http://example.com/verify/{instance.pk}/"  # Placeholder
        send_mail(
            'Verify your account',
            f'Click the link to verify your account: {verification_link}',
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            fail_silently=True,
        )
