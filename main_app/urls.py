from django.urls import path
from . import views
	
  
urlpatterns = [
	path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('chapsticks/', views.chapsticks_index, name='chapsticks_index'),
  path('chapsticks/<int:chapstick_id>/', views.chapsticks_detail, name='detail'),
  path('chapsticks/create/', views.ChapstickCreate.as_view(), name='chapsticks_create'),
]

