from django.forms import ModelForm
from .models import Chewmark

class ChewmarkForm(ModelForm):
  class Meta:
    model = Chewmark
    fields = ['date', 'size']