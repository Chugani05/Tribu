"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect
import accounts.views

urlpatterns = [
    path('', lambda r: redirect('echos:echo-list')),
    path('admin/', admin.site.urls),
    path('echos/', include('echos.urls')),
    path('waves/', include('waves.urls')),
    path('users/', include('users.urls')),
    path('login/',  accounts.views.user_login, name='login'),
    path('logout/',  accounts.views.user_logout, name='logout'),
    path('signup/',  accounts.views.user_signup, name='signup')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)