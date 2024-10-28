from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Wave


def wave_detail(request: HttpRequest, wave_id: str) -> HttpResponse:
    wave = Wave.objects.get(id=wave_id)
    return render(request, 'waves/wave-detail.html', dict(wave=wave))


def add_wave(request):
    wave = form.save(commit=False)
    wave.user = request.user
    wave.echo = echo
    wave.save
    pass


def edit_wave(request, wave_id):
    pass


def delete_wave(request, wave_id):
    pass
