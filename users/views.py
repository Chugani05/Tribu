from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


@login_required
def user_list(request: HttpRequest) -> HttpResponse:
    users = User.objects.all()
    return render(request, 'users/user_list.html', dict(users=users))


@login_required
def my_profile(request: HttpRequest) -> HttpResponse:
    return redirect('users:user-detail', username=request.user)


@login_required
def user_detail(request: HttpRequest, username: str) -> HttpResponse:
    consumer = User.objects.get(username=username)
    echos = consumer.echos.all()
    last_echos = echos[:5]
    return render(request, 'users/user_detail.html', dict(consumer=consumer, echos=last_echos, quantity=len(echos)))


@login_required
def edit_profile(request: HttpRequest, username: str) -> HttpResponse:
    pass


@login_required
def user_echos(request: HttpRequest, username: str) -> HttpResponse:
    consumer = User.objects.get(username=username)
    echos = consumer.echos.all()
    return render(request, 'users/user_echos.html', dict(consumer=consumer, echos=echos))