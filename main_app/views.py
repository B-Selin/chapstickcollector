from django.shortcuts import render


chapsticks = [
  {'location': 'Office Desk', 'flavor': 'cherry', 'description': 'my daily chapstick'},
  {'location': 'Kitchen Counter', 'flavor': 'vanilla', 'description': 'use this one while baking'},
  {'location': 'Car Cup Holder', 'flavor': 'mint', 'description': 'keep this one in the car'},
  {'location': 'Left Nightstand', 'flavor': 'coconut', 'description': 'use this one before bed'},
  {'location': 'Bathroom', 'flavor': 'coconut', 'description': 'use this one while getting ready'}
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def chapsticks_index(request):
    return render(request, 'chapsticks/index.html', {
        'chapsticks': chapsticks
    })

# def chapstick_detail(request, chapstick_id):
#     return render(request, 'chapsticks/detail.html')    

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