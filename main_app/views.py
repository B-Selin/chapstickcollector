from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Chapstick



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
    return render(request, 'chapsticks/detail.html', { 'chapstick' : chapstick})    

class ChapstickCreate(CreateView):
    model = Chapstick
    fields = ['location', 'flavour', 'description']
    success_url = '/chapsticks/'
# or we can use fields = '__all__'

# def chapstick_update(request, chapstick_id):
#     pass

# def chapstick_delete(request, chapstick_id):
#     pass