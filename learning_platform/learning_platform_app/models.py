from django.db import models

<<<<<<< HEAD
# Create your models here.
=======
>>>>>>> 53dee7202975b4351683cf584b71b9914ad1ba55

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in hours")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField()
    what_you_will_learn = models.TextField(default="Nothing")
    prerequisites = models.TextField(blank=True, null=True)


    
    def __str__(self):
        return self.title