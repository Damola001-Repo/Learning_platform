from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    courses_enrolled = models.ManyToManyField('learning_platform_app.Course', blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
=======
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    courses_enrolled = models.ManyToManyField('learning_platform_app.Course', related_name='enrolled_users', blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name if self.first_name and self.last_name else self.username
>>>>>>> 53dee7202975b4351683cf584b71b9914ad1ba55
