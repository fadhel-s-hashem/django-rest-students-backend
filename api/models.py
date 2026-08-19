from django.db import models

#  almos how every model well look like 
class Student(models.Model):
    # Add the three fields.
    GENDER_CHOICES = [
        ('Male'),
        ('Female'),

    ]

    name = models.CharField(max_length=100)
    favorite_food = models.CharField(max_length=100)
    favorite_emoji = models.CharField(max_length=20)

    class Meta:
        # Add alphabetical ordering.
        ordering = ['name'] # alphabetical ordering by name

    def __str__(self):

        return self.name
