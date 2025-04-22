from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    courses_enrolled = models.ManyToManyField('Course', related_name='enrolled_users', blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    linkedin_url = models.URLField(max_length=200, blank=True, null=True)
    portfolio_url = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in hours")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField()
    what_you_will_learn = models.TextField()
    prerequisites = models.TextField(blank=True, null=True)


    
    def __str__(self):
        return self.title