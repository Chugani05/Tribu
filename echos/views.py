from django.shortcuts import render
from .models import Echo
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required


def echo_list(request: HttpRequest) -> HttpResponse:
    pass


@login_required
def add_echo(request):
    pass


def echo_detail(request: HttpRequest, echo_id: str) -> HttpResponse:
    echo = Echo.objects.get(id=echo_id)
    return render(request, 'echos/echo-detail.html', dict(echo=echo))


def edit_echo(request, echo_id):
    pass


def delete_echo(request, echo_id):
    pass


def echo_waves(request: HttpRequest) -> HttpResponse:
    pass


def add_wave(request):
    pass