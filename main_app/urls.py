from django.urls import path
from . import views
	
  
urlpatterns = [
	path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('chapsticks/', views.chapsticks_index, name='chapsticks_index'),
]