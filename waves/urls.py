from django.urls import path

from . import views

app_name = 'waves'

urlpatterns = [
    path('waves/<wave_id>/', views.wave_detail, name='wave-detail'),
    path('waves/<wave_id>/edit/', views.edit_wave, name='edit-wave'),
    path('waves/<wave_id>/delete/', views.delete_wave, name='delete-wave'),
    path('<echo_id>/waves/add/', views.add_wave, name='add-wave'),
]