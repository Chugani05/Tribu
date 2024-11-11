from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.user_list, name='user-list'),
    path('@me/', views.my_profile, name='my-profile'),
    path('<str:username>/', views.user_detail, name='user-detail'),
    path('<str:username>/edit/', views.edit_user, name='edit-user'),
    path('<str:username>/echos/', views.user_echos, name='user-echos'),
]
