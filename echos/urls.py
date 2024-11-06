from django.urls import path

from . import views

app_name = 'echos'

urlpatterns = [
    path('', views.echo_list, name='echo-list'),
    path('add/', views.add_echo, name='add-echo'),
    path('int: <echo_id>/', views.echo_detail, name='echo_detail'),
    path('<echo_id>/edit/', views.edit_echo, name='edit-echo'),
    path('<echo_id>/delete/', views.delete_echo, name='delete-echo'),
    path('<echo_id>/waves/', views.echo_waves, name='echo-waves'),
]