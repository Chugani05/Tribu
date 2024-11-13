from django.urls import path

from . import views

app_name = 'waves'

urlpatterns = [
    path('waves/<int:wave_pk>/', views.wave_detail, name='wave-detail'),
    path('waves/<int:wave_pk>/edit/', views.edit_wave, name='edit-wave'),
    path('waves/<int:wave_pk>/delete/', views.delete_wave, name='delete-wave'),
]