from django.urls import path
from . import views
	
  
urlpatterns = [
	path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('chapsticks/', views.chapsticks_index, name='chapsticks_index'),
  path('chapsticks/<int:chapstick_id>/', views.chapsticks_detail, name='detail'),
  path('chapsticks/create/', views.ChapstickCreate.as_view(), name='chapsticks_create'),
  path('chapsticks/<int:pk>/update/', views.ChapstickUpdate.as_view(), name='chapsticks_update'),
  path('chapsticks/<int:pk>/delete/', views.ChapstickDelete.as_view(), name='chapsticks_delete'),
  path('chapsticks/<int:chapstick_id>/add_chewmark/', views.add_chewmark, name='add_chewmark'),
  path('chapsticks/<int:chapstick_id>/assoc_sidekick/<int:sidekick_id>/', views.assoc_sidekick, name='assoc_sidekick'),
  path('chapsticks/<int:chapstick_id>/unassoc_sidekick/<int:sidekick_id>/', views.unassoc_sidekick, name='unassoc_sidekick'),
  path('sidekicks/', views.SidekickList.as_view(), name='sidekicks_index'),
  path('sidekicks/<int:pk>/', views.SidekickDetail.as_view(), name='sidekicks_detail'),
  path('sidekicks/create/', views.SidekickCreate.as_view(), name='sidekicks_create'),
  path('sidekicks/<int:pk>/update/', views.SidekickUpdate.as_view(), name='sidekicks_update'),
  path('sidekicks/<int:pk>/delete/', views.SidekickDelete.as_view(), name='sidekicks_delete'),
]

