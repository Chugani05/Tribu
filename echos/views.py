from django.shortcuts import render
from .models import Echo
from django.http import HttpRequest, HttpResponse


def echo_list(request: HttpRequest) -> HttpResponse:


def add_echo(request):


def echo_detail(request: HttpRequest, echo_id: str) -> HttpResponse:
    echo = Echo.objects.get(id=echo_id)
    return render(request, 'echos/echo-detail.html', dict(echo=echo))

def edit_echo(request, echo_id):


def delete_echo(request, echo_id):


def echo_waves(request: HttpRequest) -> HttpResponse:


def add_wave(request):