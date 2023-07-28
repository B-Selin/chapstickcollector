from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Chapstick
from .forms import ChewmarkForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def chapsticks_index(request):
    chapsticks = Chapstick.objects.all()
    return render(request, 'chapsticks/index.html', { 'chapsticks': chapsticks })

def chapsticks_detail(request, chapstick_id):
    chapstick = Chapstick.objects.get(id=chapstick_id)
    chewmark_form = ChewmarkForm()
    return render(request, 'chapsticks/detail.html', {
    # include the chapstick and chewmark_form in the context
    'chapstick': chapstick, 'chewmark_form': chewmark_form
    })

def add_chewmark(request, chapstick_id):
  # create a ModelForm instance using the data in request.POST
  form = ChewmarkForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_chewmark = form.save(commit=False)
    new_chewmark.chapstick_id = chapstick_id
    new_chewmark.save()
  return redirect('detail', chapstick_id=chapstick_id)

class ChapstickCreate(CreateView):
    model = Chapstick
    fields = ['location', 'flavour', 'description']
    success_url = '/chapsticks/'
# or we can use fields = '__all__'

class ChapstickUpdate(UpdateView):
  model = Chapstick
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['location', 'flavour', 'description']

class ChapstickDelete(DeleteView):
  model = Chapstick
  success_url = '/chapsticks'