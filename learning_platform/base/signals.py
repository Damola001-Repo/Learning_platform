from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Student


@receiver(post_save, sender=CustomUser)
def create_student_profile(sender, instance, created, **kwargs):
    if created and instance.role == CustomUser.STUDENT:
        Student.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name)