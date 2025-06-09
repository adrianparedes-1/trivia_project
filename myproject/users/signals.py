from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Users

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # Create a profile if a new User instance is created
    if created:
        Users.objects.create(user=instance)
    else:
        # Save the profile for existing users (if needed)
        instance.profile.save()