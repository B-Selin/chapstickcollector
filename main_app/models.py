from django.db import models
from django.urls import reverse

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
  
  def get_absolute_url(self):
      return reverse('detail', kwargs={'chapstick_id': self.id}) 