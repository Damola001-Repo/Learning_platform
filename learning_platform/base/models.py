from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    STUDENT = 'student'
    INSTRUCTOR = 'instructor'
    ROLE_CHOICES = [
        (STUDENT, 'Student'),
        (INSTRUCTOR, 'INstructor'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=STUDENT)
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student')
    avatar = models.ImageField(null=True, default='avatar.svg')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    progress = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.email
    
class Instructor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='instructor')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    avatar = models.ImageField(null=True, default='avatar.svg')
    bio = models.TextField(blank=True)
    expertise = models.CharField(max_length=255)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.email

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(null=True, default='course_thumbnail.jpg')
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True, related_name='courses')
    rating = models.FloatField(default=0.0) 
    price = models.DecimalField(max_digits=8, decimal_places=2)
    starting_date = models.DateField(default=now)

    def __str__(self):
        return self.title
    
class WhatYouWillLearn(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='learning')
    item = models.CharField(max_length=255)

    def __str__(self):
        return self.item
    
class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=255)
    order = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"{self.course.title} - {self.title}"
    
class Topic(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='topic')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class Project(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    
class Lecture(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='lectures')
    title = models.CharField(max_length=255)
    order = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"{self.section.title} - {self.title}"
    
    

class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, related_name='enrollments')
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, related_name='enrollments')
    enrolled_on = models.DateField(auto_now_add=True)
    progress = models.FloatField(default=0.0)