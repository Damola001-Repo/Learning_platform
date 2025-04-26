from .models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            first_name = user.first_name,
            last_name = user.last_name,
            email=user.email
        )


post_save.connect(createProfile, sender=User)