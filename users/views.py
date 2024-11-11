from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse


def user_list(request: HttpRequest) -> HttpResponse:
    users = User.objects.all()
    return render(request, 'users/user_list.html', dict(users=users))


def my_profile(request: HttpRequest) -> HttpResponse:
    return redirect(reverse('users/my_profile.html', kwargs={'username': request.user.username}))


def user_detail(request: HttpRequest, username: str) -> HttpResponse:
    consumer = User.objects.get(username=username)
    return render(request, 'users/user_detail.html', dict(user=consumer))


def edit_user():
    pass


def user_echos():
    pass
