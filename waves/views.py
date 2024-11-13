from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Wave
from .forms import AddWaveForm


@login_required
def wave_detail(request: HttpRequest, wave_pk: str) -> HttpResponse:
    wave = Wave.objects.get(pk=wave_pk)
    return render(request, 'waves/wave_detail.html', dict(wave=wave))


@login_required
def edit_wave(request: HttpRequest, wave_pk: str) -> HttpResponse:
    wave = Wave.objects.get(pk=wave_pk)
    if wave.user != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        if (form := AddWaveForm(request.POST, instance=wave)).is_valid():
            wave = form.save(commit=False)
            wave.id = wave_pk
            wave.save()
            return redirect('echos:echo-list')
    else:
        form = AddWaveForm(instance=wave)
    return render(request, 'waves/edit_wave.html', dict(form=form, wave=wave))


@login_required
def delete_wave(request: HttpRequest, wave_pk: str) -> HttpResponse:
    wave = Wave.objects.get(pk=wave_pk)
    if wave.user != request.user:
        return HttpResponseForbidden()
    wave.delete()
    return render(request, 'waves/delete_wave.html', dict(wave=wave))
