from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in hours")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField()

    
    def __str__(self):
        return self.title