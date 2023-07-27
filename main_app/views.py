from django.shortcuts import render
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



# def chapstick_create(request):
#     if request.method == 'POST':
#         # create chapstick from form data
#         pass
#     else:
#         # show form
#         pass

# def chapstick_update(request, chapstick_id):
#     pass

# def chapstick_delete(request, chapstick_id):
#     pass