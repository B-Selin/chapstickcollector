from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
SIZE = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large')
)

# create a chapstick sidekick personama with name and super power ability, that we will associate with the chapstick

class Sidekick(models.Model):
  name = models.CharField(max_length=50)
  power = models.CharField(max_length=120)

  def __str__ (self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('sidekicks_detail', kwargs={'pk': self.id})



class Chapstick(models.Model):
  location = models.CharField(max_length=100)
  flavour = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  sidekicks = models.ManyToManyField(Sidekick)


  # Changing this instance method
  # does not impact the database, therefore
  # no makemigrations is necessary
  def __str__(self):
    return f'{self.location} ({self.id})'
  
  def get_absolute_url(self):
      return reverse('detail', kwargs={'chapstick_id': self.id}) 
  
  # include a method to count for total bitemarksa on each chapstick
  def count_chewmarks(self):
    return self.chewmark_set.count()
# make a new model here called ChewMarks

class Chewmark(models.Model):
  date = models.DateField()
  size = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=SIZE,
    # set the default value for bite to be 'S'
    default=SIZE[0][0]
   )
  chapstick = models.ForeignKey(Chapstick, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_size_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']

