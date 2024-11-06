from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Wave


def wave_detail(request: HttpRequest, wave_pk: str) -> HttpResponse:
    wave = Wave.objects.get(id=wave_pk)
    return render(request, 'waves/wave-detail.html', dict(wave=wave))


def edit_wave(request, wave_pk):
    pass


def delete_wave(request, wave_pk):
    pass
