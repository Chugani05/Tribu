from django.shortcuts import render
from .models import Wave


def wave_detail(request: HttpRequest, wave_id: str) -> HttpResponse:
    wave = Wave.objects.get(pk=wave_id)
    return render(request, 'waves/wave-detail.html', dict(wave=wave))


def edit_wave(request, wave_id):


def delete_wave(request, wave_id):