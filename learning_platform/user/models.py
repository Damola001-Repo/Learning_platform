from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    courses_enrolled = models.ManyToManyField('learning_platform_app.Course', related_name='enrolled_users', blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name if self.first_name and self.last_name else self.username