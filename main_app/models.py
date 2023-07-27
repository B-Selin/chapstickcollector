from django.db import models

# Create your models here.

class Chapstick(models.Model):
  location = models.CharField(max_length=100)
  flavour = models.CharField(max_length=100)
  description = models.TextField(max_length=250)


  # Changing this instance method
  # does not impact the database, therefore
  # no makemigrations is necessary
  def __str__(self):
    return f'{self.location} ({self.id})'