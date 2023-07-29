from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Chapstick, Sidekick
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
    id_list = chapstick.sidekicks.all().values_list('id')
    sidekicks_chapstick_doesnt_have = Sidekick.objects.exclude(id__in=id_list)

    chewmark_form = ChewmarkForm()
    return render(request, 'chapsticks/detail.html', {
    # include the chapstick and chewmark_form in the context
    'chapstick': chapstick, 'chewmark_form': chewmark_form,
    'sidekicks': sidekicks_chapstick_doesnt_have
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


class SidekickList(ListView):
  model = Sidekick

class SidekickDetail(DetailView):
  model = Sidekick

class SidekickCreate(CreateView):
  model = Sidekick
  fields = '__all__'

class SidekickUpdate(UpdateView):
  model = Sidekick
  fields = ['name', 'power']

class SidekickDelete(DeleteView):
  model = Sidekick
  success_url = '/sidekicks'


def assoc_sidekick(request, chapstick_id, sidekick_id):
  Chapstick.objects.get(id=chapstick_id).sidekicks.add(sidekick_id)
  return redirect('detail', chapstick_id=chapstick_id)

def unassoc_sidekick(request, chapstick_id, sidekick_id):
  Chapstick.objects.get(id=chapstick_id).sidekicks.remove(sidekick_id)
  return redirect('detail', chapstick_id=chapstick_id)